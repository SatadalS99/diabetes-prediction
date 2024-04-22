import uvicorn
from fastapi import FastAPI
from DiabeticModels import DiabeticModel
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object

#creating app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


@app.get('/')
def message():
    return {'message': 'Hi there'}



@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to the project ': f'{name}'}



@app.post('/predict')
def predict_diabetes(data: DiabeticModel):
    
    data = data.dict()
    preg = data['Pregnancies']
    glu = data['Glucose']
    bp = data['BloodPressure']
    skin = data['SkinThickness']
    insulin = data['Insulin']
    bmi = data['BMI']
    dpf = data['DiabetesPedigreeFunction']
    age = data['Age']

        
    prediction = classifier.predict([[preg, glu, bp, skin, insulin, bmi, dpf, age]])
    
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
  
 ####uvicorn app:app --reload 