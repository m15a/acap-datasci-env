ARG VERSION=3.6.4
FROM prefecthq/prefect:${VERSION}-python3.13
ENV PREFECT_SERVER_ANALYTICS_ENABLED=false
EXPOSE 4200
ENTRYPOINT ["prefect", "server"]
CMD ["start", "--host", "0.0.0.0"]
