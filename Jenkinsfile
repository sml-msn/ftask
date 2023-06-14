pipeline {
    agent any

    stages {
        stage('docker') {
            steps {
               sh 'docker build -t mytag -f Dockerfile .'
            }
        }
    }
}
