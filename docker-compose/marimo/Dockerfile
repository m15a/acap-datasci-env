FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim
RUN useradd -m appuser \
    && mkdir -p /app/work /app/venv /home/appuser/.config/marimo \
    && chown -R appuser:appuser /app /home/appuser
VOLUME ["/app/venv", "/home/appuser/.config/marimo"]
USER appuser
ENV UV_SYSTEM_PYTHON=1 \
    UV_PROJECT=/app \
    UV_PROJECT_ENVIRONMENT=/app/venv
WORKDIR $UV_PROJECT
COPY --chown=appuser:appuser pyproject.toml ./
RUN uv sync
WORKDIR /app/work
EXPOSE 2718
ENTRYPOINT ["uv", "run", "marimo"]
CMD ["edit", "--no-token", "--host=0.0.0.0"]
