from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, routes
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# build out routes
# containerize w/ Docker
# deploy to AWS (EC2?)

@app.get("/")
async def read_root():
    return {'message': "Ready to handle your biggest tasks!"}

# get all tasks
@app.get('/tasks')
async def read_tasks():
    return

# get task by ID
@app.get('tasks/{taskId}')
def read_task(taskId: int):
    return

# create task
@app.post("/tasks/", response_model=models.Task)
async def create_task(task: models.Task, db: AsyncSession = Depends(get_db)):
    await routes.create_task(db, task=task)
    return {'message': 'Task created'}

# delete task
@app.delete('/tasks/{taskId}')
async def delete_task(taskId: int):
    return
