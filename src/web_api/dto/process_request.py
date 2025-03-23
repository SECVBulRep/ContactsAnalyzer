from pydantic import BaseModel
from typing import List

class ProcessRequest(BaseModel):
    llm_type: str
    display_names: List[str]