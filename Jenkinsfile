pipeline {
    agent {
        docker {
            image 'python:3.7.9'
            args ' -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        registry = 'birdi7/devops:jnks'
        registryCredential = 'dockerhubCredentials'
        dockerImage = ''
        workdir = 'app_python'
    }

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python dependencies') {
            steps {
                sh 'pip install -r app_python/requirements.txt'
                sh 'pip install -r app_python/requirements-dev.txt'
            }
        }

        stage('Linting and formatting') {
            steps {
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
                sh 'flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics'
                sh 'black --check .'
            }
        }

        stage('Unit tests') {
            steps {
                sh 'make test'
            }
        }

        stage('install docker') {
            steps {
                sh 'apt-get update; apt-get install curl -y'
                sh 'curl -fsSL https://get.docker.com | sh'
            }
        }
        stage('Build docker image') {
            steps{
                dir(path: workdir) {
                    script {
                        dockerImage = docker.build registry + ":jenkins-$BUILD_NUMBER"
                    }
                }
            }
        }

        stage('Deploy docker image') {
            steps{
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
