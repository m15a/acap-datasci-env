FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
ENV UV_SYSTEM_PYTHON=1
COPY requirements.txt.prefect /tmp/
COPY requirements.txt /tmp/
RUN uv pip install --no-cache \
    -r /tmp/requirements.txt.prefect \
    -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt.prefect /tmp/requirements.txt
RUN useradd -m nonroot \
    && mkdir -p /work \
    && chown nonroot:nonroot /work
USER nonroot
WORKDIR /work
EXPOSE 2718
CMD ["marimo", "edit", "--no-token", "--host=0.0.0.0"]
