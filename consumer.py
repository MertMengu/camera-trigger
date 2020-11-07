import pika
import pymongo
from pymongo import MongoClient
import json

queueConnection = None
connectionParameters = pika.URLParameters('amqps://bzhfxmiu:704BL6PjJwIIRofh9oiCV0gYMZ644YgN@roedeer.rmq.cloudamqp.com/bzhfxmiu')
consumerChannel = None

mongoCluster = MongoClient('mongodb+srv://unrivallled:6gCWFj6zA7N8RQBX@development.vigsh.mongodb.net')
db = mongoCluster['cameralyze']
collection = db['logs']

def getChannel():
    global queueConnection
    global consumerChannel
    if queueConnection is None:
        queueConnection = pika.BlockingConnection(connectionParameters)
        print('Queue connection initialized for consumer')
        consumerChannel = queueConnection.channel()
        
    return consumerChannel

channel = getChannel()
channel.queue_declare(queue='logs')

def callback(ch, method, properties, body):
    message = json.loads(json.loads(body))
    print(" [x] Received %r" % message)
    collection.insert_one(message)

channel.basic_consume(queue='logs', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages to consume')
channel.start_consuming()