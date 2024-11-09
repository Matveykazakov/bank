from fastapi import FastAPI
from aiokafka import AIOKafkaProducer
import json
from dtos import ConversionDTO

app = FastAPI()
producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')

@app.on_event("startup")
async def startup_event():
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()

@app.post("/convert")
async def convert_currency(conversion: ConversionDTO):
    converted_amount = conversion.amount * 1.1  # указываем конверсию
    conversion_result = {
        "from_currency": conversion.from_currency,
        "to_currency": conversion.to_currency,
        "converted_amount": converted_amount
    }
    await producer.send_and_wait("conversion_topic", json.dumps(conversion_result).encode('utf-8'))
    return conversion_result
