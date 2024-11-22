import time
from flask import Flask, request, jsonify

app = Flask(__name__)

EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.9,
    "JPY": 110.0
}

# Функция для ожидания Kafka
def wait_for_kafka(host, port, retries=10, delay=5):
    for i in range(retries):
        try:
            print("Kafka is ready!")
            return
        except Exception:
            print(f"Kafka not available. Retrying in {delay} seconds... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("Kafka is not available after retries!")

# Ожидание Kafka перед запуском сервиса
wait_for_kafka("kafka", 9092)

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    if not data or 'amount' not in data or 'from_currency' not in data or 'to_currency' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    amount = data['amount']
    from_currency = data['from_currency']
    to_currency = data['to_currency']

    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        return jsonify({"error": "Invalid currencies"}), 400

    converted_amount = amount * EXCHANGE_RATES[to_currency] / EXCHANGE_RATES[from_currency]
    return jsonify({"converted_amount": converted_amount}), 200

@app.route("/")
def home():
    return "Valute Converter Service is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
