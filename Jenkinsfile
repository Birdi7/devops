pipeline {
    agent { docker { image 'python:3.7.9' } }
    stages {
        stage('test') {
            steps {
                sh 'pip install -r app_python/requirements.txt'
                sh 'pip install -r app_python/requirements-dev.txt'
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
                sh 'flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics'
                sh 'black --check .'
                sh 'make test'
            }
        }
    }
}
