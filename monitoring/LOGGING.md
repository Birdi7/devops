# Logging
## Screenshots

![](images/1.png)
![](images/2.png)

App's whole logging system is configured to put logs into `/tmp/app_python.log` file,
then here is the path
`app container -> VM -> host system -> VM -> promtail container`
idk if host is actually involved here, but I have the file on the host file system


## Found bugs

There is an interesting point of doing this lab
on MacOS in particular. The docker actually runs
in the special, vm created by `docker desktop`, and docker mounts only a specified folders to the mentioned
VM.
![](images/3.png)

Also, it doesn't work with `/var/log` dir — because of some `PermissionError` exception


## Best practices
1. Performs log rotate either based on log size or time. Use `RotatingFileHandler` or `TimedRotatingFileHandler`
for this on python
2. Put backups on a `s3` storage or whatever storage
3. Put loki database on `s3` or any other persistent storage. [examples](https://grafana.com/docs/loki/latest/storage/)
4. Use one format consistently, so that it's easy to parse them
5. Use `alert management system`. For instance, if `healthcheck` failed
6. Use [sentry](sentry.io) for errors, as it's easier to analyze the software outcome than the raw logs

# Metrics

Very useful — https://docs.docker.com/config/daemon/prometheus/

![](images/4.png)
![](images/5.png)
![](images/6.png)
![](images/7.png)
![](images/8.png)
![](images/9.png)
![](images/10.png)
![](images/11.png)
