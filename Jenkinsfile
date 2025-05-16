pipeline {
    agent any

    environment {
        // Укажите полный путь к python3/pip
        PYTHON_PATH = '/usr/bin/python3'  // Linux/Mac
        // ИЛИ для Windows:
        // PYTHON_PATH = 'C:\\Python39\\python.exe'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh """
                    ${env.PYTHON_PATH} -m pip install --upgrade pip
                    ${env.PYTHON_PATH} -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh '${env.PYTHON_PATH} -m pytest tests/ --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
            cleanWs()
        }
    }
}