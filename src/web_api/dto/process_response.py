from pydantic import BaseModel


class ProcessResponse(BaseModel):
    output: str
