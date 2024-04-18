from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

db = []

class City(BaseModel):
    name:str
    timezone: str

@app.get("/")
def hello():
    return {"mm": "안녕하세요 파이보"}

@app.get('/cities')
def get_cities():
    results = []    
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time})
    return results

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)
    
    cur_time = r.json()['datetime']
    
    return {'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time}

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())    
    return db[-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    
    return {}