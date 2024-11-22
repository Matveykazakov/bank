# Bank System Microservices
## Архитектура

Проект состоит из нескольких микросервисов, взаимодействующих через API и очередь сообщений Kafka. Система использует Redis для хранения данных о транзакциях и Kafka для обработки событий.

### Используемые технологии:
- **Flask** для создания веб-приложений и обработки HTTP-запросов.
- **Kafka** для асинхронной обработки и обмена сообщениями между микросервисами.
- **Redis** для хранения данных транзакций.
- **Docker** для контейнеризации сервисов.
- **HTML/CSS/JavaScript** для фронтенд-формы отправки транзакций.

## Запуск проекта

Для удобства развертывания всех сервисов и их взаимодействия используется Docker и Docker Compose.

### Шаги для запуска:

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/Matveykazakov/bank
   cd project
2. **Создайте образ и запустите контейнеры с помощью Docker Compose**:
   ```bash
   docker-compose up --build

## Пример отправки транзакции
![image](https://github.com/user-attachments/assets/34a653d8-6aa6-4d49-b5f5-78b5d35e8da7)
## Результат:
![image](https://github.com/user-attachments/assets/404e3372-34d3-4ee0-b61b-3041f74991bb)
![image](https://github.com/user-attachments/assets/2a0f6825-e6dc-45f6-abe4-948e1e1cd17b)

