from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Task
from .typings import TaskInterface

async def create_task(db: AsyncSession, task: TaskInterface):
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task
