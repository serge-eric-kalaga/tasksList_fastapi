from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import uvicorn
from colorama import init
from typing import Union
from models import TaskModel

app = FastAPI()

tasks_list = []

@app.get('/task')
def all_tasks():
    """Return all the tasks"""
    return tasks_list

@app.get("/task/{task_id}")
def one_task(task_id: int):
    t = None
    for task in tasks_list :
        if task.id == task_id :
            t = task
    return t

@app.post("/task")
def add_task(task: TaskModel):
    tasks_list.append(task)
    return task

@app.put("/task/{task_id}")
def edit_task(task_id: int, task: TaskModel):
    for t in tasks_list:
        if t.id == task_id :
            t.id = task.id
            t.name = task.name
            t.description = task.description
            break
        else : raise HTTPException(404)



@app.delete("/task/{task_id}")
def edit_task(task_id: int):
    for t in tasks_list:
        if t.id == task_id :
            tasks_list.pop(task_id)
        else : raise HTTPException(404)
    
            

  
if __name__ == "__main__":
    init()
    uvicorn.run("main:app", host="0.0.0.0", reload=True)