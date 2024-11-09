from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
import json
from dtos import TransactionDTO

app = FastAPI()
consumer = AIOKafkaConsumer('transaction_topic', bootstrap_servers='kafka:9092')

@app.on_event("startup")
async def startup_event():
    await consumer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await consumer.stop()

@app.get("/process-transactions")
async def process_transactions():
    async for msg in consumer:
        transaction = json.loads(msg.value.decode('utf-8'))
        print(f"Processing transaction: {transaction}")
    return {"status": "Processing"}
