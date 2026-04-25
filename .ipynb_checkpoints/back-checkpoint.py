from fastapi import FastAPI, Request, HTTPException, Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import joblib
class Features(BaseModel):
    features:list[float]

model=joblib.load("model.pkl")
def pred(feature):
    prediction=model.predict([feature])
    return prediction.tolist()
@app.get("/")
def home():
    return {"Hello World"}

@app.post("/predict")
def Prediction(data:Features):
    try:
        return {"Prediction":pred(data.features)}
    except Exception as e:
        raise HTTPException (status_code=404,detail=e)


