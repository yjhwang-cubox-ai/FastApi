from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import requests

app = FastAPI()

class ToDo(BaseModel):
    title: str
    contents: str
    date: datetime
    
db = []
    
@app.get("/")
def init():
    return {"message":"ToDo List"}

@app.get("/todo")
def get_todo_list():
    return db

@app.post("/todo")
def post_todo(todo: ToDo):
    date_adress = "http://worldtimeapi.org/api/timezone/Asia/Seoul"
    r = requests.get(date_adress)
    curtime = r.json()['datetime']
    
    todo.date = curtime
    
    db.append(dict(todo))
    
    return todo

@app.put("/todo/{todo_id}")
def modify_todo(todo_id: int, todo: ToDo):
    date_adress = "http://worldtimeapi.org/api/timezone/Asia/Seoul"
    r = requests.get(date_adress)
    curtime = r.json()['datetime']
    
    todo.date = curtime
    
    db[todo_id-1] = todo
    
    return db[todo_id-1]

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    db.pop(todo_id-1)
    return {}
    