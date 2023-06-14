pipeline {
    agent any

    stages {
        stage('tests') {
            steps {
               sh 'pytest tests.py --datapath testdata/m_test.csv --modelpath models/cat_clf_mdl.joblib'
            }
        }
        stage('docker') {
            steps {
               sh 'docker build -t mytag -f Dockerfile .'
            }
        }
    }
}
