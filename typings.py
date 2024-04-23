from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskInterface(BaseModel):
    id: int
    title: str
    description: str
    is_complete: bool
    date_created: datetime
    date_completed: Optional[datetime]
