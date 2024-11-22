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
![image](https://github.com/user-attachments/assets/f3f37f01-cd81-4494-90bb-c85f56a2fc69)
## Результат:
![image](https://github.com/user-attachments/assets/4107c3fc-e52b-4ba4-b91d-3d6d0d364ba3)
![image](https://github.com/user-attachments/assets/3088171b-a844-4c4e-beee-5ff1d305ce4f)
