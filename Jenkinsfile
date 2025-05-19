pipeline {
    agent any

    stages {
        stage('Run tests in Docker') {
            steps {
                sh '''
                    echo "🐳 Запускаем тесты внутри Docker-контейнера"

                    docker run --rm \
                        -v "$PWD":/app \
                        -w /app \
                        my-python313-aqa:latest \
                        bash -c "
                            python3 -m venv venv && \
                            . venv/bin/activate && \
                            pip install --upgrade pip && \
                            pip install -r requirements.txt && \
                            pytest tests/ --alluredir=allure-results --junitxml=junit-results.xml
                        "
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
