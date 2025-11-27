ARG VERSION=3.6.4
FROM prefecthq/prefect:${VERSION}-python3.13
COPY requirements.txt /tmp/
RUN uv pip install --no-cache -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
ENTRYPOINT ["prefect", "worker"]
