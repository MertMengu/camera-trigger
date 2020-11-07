import pika
from logModel import LogModel
import json

queueConnection = None
connectionParameters = pika.URLParameters('amqps://bzhfxmiu:704BL6PjJwIIRofh9oiCV0gYMZ644YgN@roedeer.rmq.cloudamqp.com/bzhfxmiu')
publisherChannel = None

def getChannel():
    global queueConnection
    global publisherChannel
    if queueConnection is None:
        queueConnection = pika.BlockingConnection(connectionParameters)
        print('Queue connection initialized for publisher')
        publisherChannel = queueConnection.channel()
        publisherChannel.queue_declare(queue='logs')
        
    return publisherChannel

def publish(logData):
    channel = getChannel() 
    channel.basic_publish(exchange='',
                          routing_key='logs',
                        body=json.dumps(logData))
