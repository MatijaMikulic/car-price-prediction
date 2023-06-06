from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict 

app = FastAPI()

class Car(BaseModel):
    odometer:int
    age:int
    manufacturer:str
    model:str
    condition:str
    cylinders:str
    transmission:str
    drive:str

@app.post("/predict")
def predict_price(car: Car):
    price=predict(car)
    return {"Price": price}

@app.get("/")
def about():
    return{
        "Info": "This API serves for car price prediction. use an HTTP POST request to the /predict endpoint",

        "Odometer":"Integer",
        "Age":"Integer",
        "Manufacturers":"chevrolet | ford | honda | nissan |toyota",
        "Models" : "camry | civic | corolla | cr-v | cruze | equinox | escape | explorer |\
f-150 | focus | fusion | impala | malibu | mustang | odyssey | prius | rav4 | silverado | silverado 1500 |\
silverado 2500hd | tacoma | tahoe | tundra",
        "Condition": "excellent | fair | good | like new | salvage | unknown",
        "Cylinders": "4 | 6 | 8 | other",
        "Transmission": "automatic | manual | other",
        "Drive": "4wd | fwd | rwd | unknown"        
    }





