from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

db = []

class City(BaseModel):
    name:str
    timezone: str
    
class CityModify(BaseModel):
    id: int
    name: str
    timezone: str
    
template = Jinja2Templates(directory="templates")


@app.get("/")
def hello():
    return {"hello": "world"}

@app.get('/cities', response_class=HTMLResponse)
def get_cities(request:Request):
    context = {}
    
    rsCity = []
    
    cnt = 0
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        
        cnt +=1
        
        rsCity.append({'id':cnt, 'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time})
    
    context['request'] = request
    context['rsCity'] = rsCity
    return template.TemplateResponse('city_list_refer.html', context)

@app.get('/cities/{city_id}')
def get_city(request:Request, city_id: int):
    city = db[city_id-1]
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
    cur_time = r.json()['datetime']
    
    context = {'request': request, 'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time}
    
    return template.TemplateResponse('city_detail.html', context)

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.put('/cities')
def modif_city(city: CityModify):
    
    db[city.id -1] = {'name':city.name, 'timezone':city.timezone}
    
    return db[city.id -1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    
    return {}