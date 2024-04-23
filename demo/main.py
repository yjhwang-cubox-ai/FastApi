from fastapi import FastAPI, Request
import requests
from db import session
from model import ToDoTable, ToDo
from typing import List

app = FastAPI()

db = []

@app.get("/")
def init():
    return "ToDo"

@app.get("/todo")
def get_todo_list(request: Request):
    
    todo_list = session.query(ToDoTable).all()
    
    return todo_list

@app.post("/todo")
def create_todo(title: str, contents: str):
    table = ToDoTable()
    table.title = title
    table.contents = contents
    
    strs = f"http://worldtimeapi.org/api/timezone/Asia/Seoul"
    r = requests.get(strs)
    curtime = r.json()['datetime']
    table.date = str(curtime)
    
    session.add(table)
    session.commit()       
    
    return "created..."

@app.put("/todo/{todo_id}")
def update_todo(todo_list: List[ToDo]):
    print("tod_list:", todo_list)
    
    for i in todo_list:
        todo = session.query(ToDoTable).filter(ToDoTable.id == i.id).first()
        todo.title = i.title
        todo.contents = i.contents
        session.commit()
    
    return "updated ... "

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    
    table = session.query(ToDoTable).filter(ToDoTable.id == todo_id).delete()
    session.commit()
    
    return "deleted ... "