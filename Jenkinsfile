pipeline {
    agent {
        docker {
            image 'python:3.7.9'
            args ' -v /var/run/docker.sock:/var/run/docker.sock'
        }
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
                // sh 'pip install -r app_python/requirements-dev.txt'
            }
        }

        stage('Linting and formatting') {
            steps {
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
                // sh 'flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics'
                // sh 'black --check .'
            }
        }

        stage('Unit tests') {
            sh 'make test'

        }

        // stage('Build docker image') {
        //     steps{
        //     script {
        //         dockerImage = docker.build registry + ":jenkins-$BUILD_NUMBER"
        //     }
        //     }
        //     }
        // }

        // stage('Deploy docker image') {
        // steps{
        //     script {
        //     docker.withRegistry('', registryCredential) {
        //         dockerImage.push()
        //     }
        //     }
        // }
        // }
    }
}
