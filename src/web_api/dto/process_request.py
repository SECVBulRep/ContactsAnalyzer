from pydantic import BaseModel

class ProcessRequest(BaseModel):
    model: str
    prompt: str