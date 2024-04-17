from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    strs = "http://worldtimeapi.org/api/timezone/Asia/Seoul"
    for city in db:
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({})
    
    
    return results

# @app.get('/cities/{city_id}')
# def get_city(city_id: int):

# @app.get('/cities')
# def create_city(city_id: int):

# @app.get('/cities/{city_id}')
# def delete_city(city_id: int):