pipeline {
    agent none
    stages {
        stage ('Back-end') {
            agent {
                docker { image 'python:2-alpine' }
            }

            steps {
                sh 'python --version'
            }
        }
    }

}