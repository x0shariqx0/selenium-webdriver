pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/x0shariqx0/selenium-webdriver.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t selenium-test .'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'docker run --rm selenium-test'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -af'
        }
    }
}
