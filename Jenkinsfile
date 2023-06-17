pipeline {
    agent any

    stages {
        stage('tests') {
            steps {
               sh 'pip3 install -r requirements.txt'
               sh '[ ! -d "datasets" ] && mkdir datasets'
               sh 'python3 -m pytest tests.py --datapath testdata/m_test.csv --modelpath models/cat_clf_mdl.joblib'
            }
        }
        stage('docker') {
            steps {
               sh 'docker build -t mytag -f Dockerfile .'
            }
        }
    }
}
