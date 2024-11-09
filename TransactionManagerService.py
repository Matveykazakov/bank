from fastapi import FastAPI, HTTPException
from aiokafka import AIOKafkaProducer
import aioredis
from dtos import TransactionDTO
import json

app = FastAPI()
producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')
redis = aioredis.from_url("redis://localhost")

@app.on_event("startup")
async def startup_event():
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()

@app.post("/transactions")
async def create_transaction(transaction: TransactionDTO):
    await producer.send_and_wait("transaction_topic", json.dumps(transaction.dict()).encode('utf-8'))
    await redis.set(f"transaction:{transaction.transaction_id}", json.dumps(transaction.dict()))
    return {"status": "Transaction sent to Kafka"}

@app.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: str):
    transaction = await redis.get(f"transaction:{transaction_id}")
    if transaction:
        return json.loads(transaction)
    raise HTTPException(status_code=404, detail="Transaction not found")
