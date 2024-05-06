import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

with open('xgb.pkl','rb') as file:
    xgb = pickle.load(file)

app = FastAPI()

class request(BaseModel):
    age : int
    housing: str
    marital : str
    job : str
    loan : str
    balance : int
    education : str
    pdays : int
    campaign : int
    month : str
    
    
@app.post("/predict")
    
def predict(data:request):
    new_data=pd.DataFrame(dict(data),index = [0])
    print('@@@@@@@@@@@@@@@@@@@@@@@@@', new_data.dtypes)

    class_idx=xgb.predict(new_data)[0]
    return int(class_idx)

 