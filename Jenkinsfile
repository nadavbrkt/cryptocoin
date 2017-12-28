pipeline {
    agent none
    stages {
        stage ('Back-end') {
            agent {
                docker { 'python:2-alpine' }
            }

            steps {
                sh 'python --version'
            }
        }
    }

}