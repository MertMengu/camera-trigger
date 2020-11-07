from fastapi import FastAPI
import publisher
from logModel import LogModel

app = FastAPI()

@app.post('/logs')
def publishLog(logData: LogModel):
    publisher.publish(logData.json())
    return { 'message': 'log data sent' }
