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
    }

}
