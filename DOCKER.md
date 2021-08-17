# Docker best practices

1. Use layer caching. Avoid to add frequently changed layer on top of the image
2. Avoid heavy images. Use [multi-stage](https://docs.docker.com/develop/develop-images/multistage-build/) builds for this purpose
3. Use `python3-alpine` if you have enough CPU for image building process
4. Use entrypoint script instead of hardcoded value in Dockerfile