from fastapi import FastAPI
from pydantic import BaseModel
import requests
from typing import Optional
from datetime import datetime

app = FastAPI()

db = []

class ToDo(BaseModel):
    title: str
    contents: str
    date: datetime

@app.get("/")
def init():
    return "ToDo"

@app.get("/todo")
def get_todo_list():
    results = []
    for todo in db:        
        results.append({'title':todo['title'], 'contents':todo['contents'], 'current_time': todo['date']})
    return results

@app.put("/todo/{todo_id}")
def get_todo(todo_id: int, todo: ToDo):
    db[todo_id-1] = dict(todo)
    return db[todo_id-1]
    

@app.post("/todo")
def create_todo(todo: ToDo):
    strs = f"http://worldtimeapi.org/api/timezone/Asia/Seoul"
    r = requests.get(strs)
    curtime = r.json()['datetime']
    todo.date = curtime
    
    db.append(dict(todo))
    return db[-1]

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    db.pop(todo_id - 1)
    
    return {}