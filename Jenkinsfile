pipeline {
    agent any

    tools {
        python "Python3"  // Требует настройки Python в Global Tool Configuration
    }

    environment {
        REPO_URL = 'https://github.com/your-username/your-repo.git'
        BRANCH = 'main'  // Или 'master', если используется старая ветка
    }

    stages {
        // Проверка наличия файлов
        stage('Check Repository') {
            steps {
                script {
                    sh '''
                        echo "Checking repository files..."
                        ls -la
                        if [ -f "requirements.txt" ]; then
                            echo "requirements.txt found"
                            cat requirements.txt
                        else
                            echo "ERROR: requirements.txt not found!"
                            exit 1
                        fi
                    '''
                }
            }
        }

        // Установка зависимостей с обработкой ошибок
        stage('Install Dependencies') {
            steps {
                script {
                    try {
                        sh '''
                            python3 -m ensurepip --upgrade
                            python3 -m pip install --upgrade pip
                            python3 -m pip install -r requirements.txt
                        '''
                    } catch (err) {
                        echo "Fallback to alternative pip installation"
                        sh '''
                            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                            python3 get-pip.py
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        // Запуск тестов с генерацией Allure-отчета
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --alluredir=allure-results'
            }

            post {
                always {
                    archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
                }
            }
        }
    }

    post {
        // Генерация отчета Allure
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
        }

        // Очистка workspace
        cleanup {
            cleanWs()
        }
    }
}