# Docker best practices

 1. Use layer caching. Avoid to add frequently changed layer on top of the image
 2. Avoid heavy images.

   Use [multi-stage](https://docs.docker.com/develop/develop-images/multistage-build/)
   builds for this purpose
 3. Use `python3-alpine` if you have enough CPU for image building proces
 4. Use entrypoint script instead of hardcoded value in CMD option of Dockerfile
 5. Use `.dockerignore` to exclude files which are not necessary for the build process. Remember — the smaller is better
 6. Each container should have only one main process. Do not put several applications in one container
