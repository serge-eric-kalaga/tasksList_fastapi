from pydantic import BaseModel
from typing import Optional

class TaskModel(BaseModel):
    id :int
    name : str
    description : Optional['str']