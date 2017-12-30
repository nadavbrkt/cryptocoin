pipeline {
    agent none
    stages {
        stage ('Back-end') {
            agent {
                docker { image 'jenkins/ssh-slave' }
            }

            steps {
                sh 'java -version'
                sh 'echo dd'
            }
        }

        stage ('front-end') {
            agent {
                docker { image 'python:2-alpine' }
            }

            steps {
                sh 'python --version'
                sh 'echo dd'
            }
        }
    }

}
