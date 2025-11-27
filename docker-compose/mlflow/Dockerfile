ARG VERSION=3.6.0
FROM ghcr.io/mlflow/mlflow:v${VERSION}
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
ENTRYPOINT ["mlflow"]
