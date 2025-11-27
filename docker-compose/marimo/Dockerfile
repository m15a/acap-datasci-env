FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
RUN useradd -m marimouser \
    && mkdir -p /work /home/marimouser/.config/marimo \
    && chown -R marimouser:marimouser /work /home/marimouser
ENV UV_SYSTEM_PYTHON=1
COPY requirements.txt /tmp/
RUN uv pip install --no-cache -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
COPY requirements.txt.prefect /tmp/
RUN uv pip install --no-cache -r /tmp/requirements.txt.prefect \
    && rm /tmp/requirements.txt.prefect
USER marimouser
WORKDIR /work
VOLUME ["/home/marimouser/.config/marimo"]
EXPOSE 2718
ENTRYPOINT ["marimo"]
CMD ["edit", "--no-token", "--host=0.0.0.0"]
