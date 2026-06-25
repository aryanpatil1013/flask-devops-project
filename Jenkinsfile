pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aryanpatil1013/flask-devops-project.git'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker compose down'
            }
        }

        stage('Build and Start') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
