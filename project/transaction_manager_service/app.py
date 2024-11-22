from kafka import KafkaProducer
import json
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

# Настройки для Kafka
KAFKA_TOPIC = 'transactions'
KAFKA_BROKER = 'kafka:9092'

# Функция для ожидания Kafka
def wait_for_kafka(host, port, retries=10, delay=5):
    for i in range(retries):
        try:
            producer = KafkaProducer(bootstrap_servers=f"{host}:{port}")
            producer.close()
            print("Kafka is ready!")
            return
        except Exception as e:
            print(f"Kafka not available. Retrying in {delay} seconds... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("Kafka is not available after retries!")

# Ожидание Kafka перед запуском сервиса
wait_for_kafka('kafka', 9092)

# Producer
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/transaction', methods=['POST'])
def send_transaction():
    try:
        data = request.json  # Извлечение данных из запроса
        if not data or 'transaction_id' not in data or 'from_account' not in data or 'to_account' not in data:
            return jsonify({"error": "Invalid transaction data"}), 400
        producer.send(KAFKA_TOPIC, value=data)
        producer.flush()  
        print(f"Transaction sent to Kafka: {data}")
        return jsonify({"status": "success", "message": "Transaction sent to Kafka."}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/')
def home():
    return "Transaction Manager Service is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
