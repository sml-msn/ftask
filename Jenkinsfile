pipeline {
    agent any

    stages {
        stage('docker') {
            steps {
                docker build -t mytag -f Dockerfile .
            }
        }
    }
}
