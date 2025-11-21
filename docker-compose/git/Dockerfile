FROM alpine:3.22.2
RUN apk add --no-cache git=~2.49.1 git-daemon=~2.49.1
VOLUME /var/www/git
RUN git config --global init.defaultBranch main
EXPOSE 9010
CMD ["git", "daemon", "--base-path=/var/www/git", "--enable=receive-pack", "--export-all", "--reuseaddr", "--verbose", "--port=9010"]
