pipeline {
    agent any

    environment {
        PYTHON = 'python3'  // Для Linux/Mac
        VENV_DIR = 'venv'
    }

    stages {
        stage('Environment Check') {
            steps {
                sh '''
                    echo "### System Info ###"
                    uname -a
                    echo "\\n### Python Version ###"
                    ${PYTHON} --version || echo "Python not found"
                    echo "\\n### Workspace Contents ###"
                    ls -la
                '''
            }
        }

        stage('Create Virtual Env') {
            steps {
                sh '''
                    echo "Creating virtual environment..."
                    ${PYTHON} -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing dependencies..."
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests..."
                    . ${VENV_DIR}/bin/activate
                    pytest tests/ \
                        --alluredir=allure-results \
                        --junitxml=junit-results.xml
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            archiveArtifacts artifacts: 'junit-results.xml', fingerprint: true

            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]

            cleanWs()
        }
    }
}
