FROM python:3.10-slim

# Обновим системные библиотеки и установим gcc только временно
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential libpq-dev \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта
COPY . .

# Запуск FastAPI (для web-сервиса)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
