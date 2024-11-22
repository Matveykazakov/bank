from kafka import KafkaConsumer
import redis
import json
import time
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS 
import os

app = Flask(__name__)

# Разрешаем CORS для всех доменов
CORS(app)

# Настройки для Kafka и Redis
KAFKA_TOPIC = 'transactions'
KAFKA_BROKER = 'kafka:9092'
REDIS_HOST = 'redis'
REDIS_PORT = 6379

# Подключение к Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

# Функция для ожидания Kafka
def wait_for_kafka(host, port, retries=10, delay=5):
    for i in range(retries):
        try:
            consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=f"{host}:{port}")
            consumer.close()
            print("Kafka is ready!")
            return
        except Exception as e:
            print(f"Kafka not available. Retrying in {delay} seconds... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("Kafka is not available after retries!")

# Ожидание Kafka перед запуском сервиса
wait_for_kafka('kafka', 9092)

def process_transaction(transaction):
    r.set(transaction['transaction_id'], json.dumps(transaction))
    print(f"Transaction {transaction['transaction_id']} stored in Redis.")

@app.route('/transaction', methods=['POST'])
def add_transaction():
    try:
        data = request.json
        required_fields = ['transaction_id', 'from_account', 'to_account', 'amount', 'currency']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        transaction_id = data['transaction_id']
        from_account = data['from_account']
        to_account = data['to_account']
        amount = data['amount']
        currency = data['currency']

        # Лог
        print(f"Processing transaction: {transaction_id} from {from_account} to {to_account} amount {amount} {currency}")
        process_transaction(data)
        
        return jsonify({"status": "success", "message": "Transaction processed successfully."}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
