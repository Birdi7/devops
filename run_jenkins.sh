#RUN FROM JENKINS SUBFOLDER

docker run --rm --name jenkins -p 8080:8080 -p 50000:50000 -u 0 -v `pwd`:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean