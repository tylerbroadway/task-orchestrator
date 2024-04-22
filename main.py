from fastapi import FastAPI
from models import Task

app = FastAPI()

# build core route
# install SQLAlchemy & postgres
# build models
# build out CRUD routes
# containerize w/ Docker
# deploy to AWS (EC2?)

# @app.get('/')

@app.get("/")
def read_root():
    return {'message': "Ready to handle your biggest tasks!"}

# get all tasks
@app.get('/tasks')
def read_tasks():
    return

# get task by ID
@app.get('tasks/{taskId}')
def read_task(taskId: int):
    return

# create
@app.post('/tasks')
def create_task(task: Task):
    return

# update
@app.patch('/tasks/{taskId}')
def update_task(taskId: int):
    return

# delete
@app.delete('/tasks/{taskId}')
def delete_task(taskId: int):
    return
