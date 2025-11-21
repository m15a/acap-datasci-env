#!/usr/bin/env python
"""Generate the Iris dataset's CSV file."""

from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris


def main() -> None:
    """Load the Iris dataset."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    df["species"] = df["target"].apply(lambda x: iris.target_names[x])
    df.to_csv(Path.cwd() / "data" / "iris.csv", index=False)


if __name__ == "__main__":
    main()
