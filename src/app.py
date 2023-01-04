from fastapi import FastAPI
from redis import Redis
from pymongo import MongoClient, errors
import pika

app = FastAPI()
host_ip = '20.24.26.103'
@app.get('/')
async def root():
    return {"message": "End of World"} 

@app.get('/redis/')
def redis_check():
    try:
        r = Redis(host=host_ip, port=6379, password='redis1234')
        r.ping()
        return {"Redis": "Connection Ok"}
    except Exception as ex:
        print(ex)
        return {"Error": "Broken"}

@app.get('/mongo/')
def mongo_check():
    try:
        client = MongoClient(host_ip, 27017)
        return {"Mongo": "Connection Ok"}
    except errors.ConnetionFailure as cf:
        return {"Error": "Broken"}

@app.get('/rabbit/')
def rabbit_check():
    try:
        creds = pika.PlainCredentials(username='admin', password='RabbitHole')
        params = pika.ConnectionParameters(host=host_ip, port='5672', credentials=creds)
        conn = pika.BlockingConnection(params)
        if conn.is_open:
            return {'Rabbit': 'Connection Open'}
        else:
            return {'Rabbit': 'Connection Closed'}
    except Exception as ex:
        print(ex)
        return {"Error": "Broken"}