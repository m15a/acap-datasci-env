"""An example of Prefect flow with MLflow tracking."""

import os
from datetime import datetime

import mlflow
import pandas as pd
from prefect import flow, task
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

MLFLOW_TRACKING_URI: str = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")


@flow
def example(n_tests: int = 1) -> None:
    """An example experiment as a Prefect flow with MLflow tracking."""
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(f"example-experiment-{datetime.now()}")

    df = pd.read_csv("s3://data/iris.csv")
    x = df.drop(columns=["target", "species"])
    y = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    test_data = x_test.copy()
    test_data["target"] = y_test
    test_dataset = mlflow.data.from_pandas(test_data, targets="target")

    @task
    def run(n_estimators, criterion) -> None:
        """A run in the experiment."""
        with mlflow.start_run():
            params = {"n_estimators": n_estimators, "criterion": criterion}
            mlflow.log_params(params)
            model = RandomForestClassifier(**params)
            model.fit(x_train, y_train)
            model_info = mlflow.sklearn.log_model(model, input_example=x_train)
            mlflow.models.evaluate(
                model=model_info.model_uri,
                data=test_dataset,
                model_type="classifier",
            )

    for n_estimators in [2**i for i in range(5, 8)]:
        for criterion in ["gini", "entropy", "log_loss"]:
            for _ in range(n_tests):
                run(n_estimators, criterion)


if __name__ == "__main__":
    example()
