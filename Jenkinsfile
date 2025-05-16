pipeline {
    agent any

    environment {
        // Для Windows укажите: PYTHON = 'python'
        PYTHON = 'python3'  // Linux/Mac
    }

    stages {
        // Этап диагностики окружения
        stage('Environment Check') {
            steps {
                sh '''
                    echo "### System Info ###"
                    uname -a
                    echo "\n### Python Version ###"
                    ${PYTHON} --version || echo "Python not found"
                    echo "\n### Pip Version ###"
                    ${PYTHON} -m pip --version || echo "Pip not installed"
                    echo "\n### Workspace Contents ###"
                    ls -la
                '''
            }
        }

        // Установка pip (если отсутствует)
        stage('Ensure Pip') {
            steps {
                sh '''
                    if ! ${PYTHON} -m pip --version &> /dev/null; then
                        echo "Installing pip..."
                        curl -sS https://bootstrap.pypa.io/get-pip.py | ${PYTHON}
                        ${PYTHON} -m ensurepip --upgrade
                    fi
                '''
            }
        }

        // Установка зависимостей
        stage('Install Dependencies') {
            steps {
                sh '''
                    ${PYTHON} -m pip install --upgrade pip
                    ${PYTHON} -m pip install -r requirements.txt
                '''
            }
        }

        // Запуск тестов
        stage('Run Tests') {
            steps {
                sh '''
                    ${PYTHON} -m pytest tests/ \
                        --alluredir=allure-results \
                        --junitxml=junit-results.xml
                '''
            }
        }
    }

    post {
        always {
            // Архивация результатов тестов
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            archiveArtifacts artifacts: 'junit-results.xml', fingerprint: true

            // Генерация Allure-отчета
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]

            // Очистка workspace
            cleanWs()
        }
    }
}