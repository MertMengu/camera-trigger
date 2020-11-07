from pydantic import BaseModel

class LogModel(BaseModel):
    name: str
    time: str
    description: str
    