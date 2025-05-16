FROM python:3.13-slim

# Базовые утилиты. Используем safe mode: без fail при ошибке
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
       curl unzip \
    || echo "apt-get failed (will try alternative)" \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Allure CLI (без лишнего)
ENV ALLURE_VERSION=2.25.0
RUN curl -sL https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip -o allure.zip && \
    unzip allure.zip -d /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure && \
    rm allure.zip

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    test -f requirements.txt && pip install -r requirements.txt || true

CMD ["bash"]
