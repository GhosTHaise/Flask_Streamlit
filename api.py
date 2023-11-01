from fastapi import FastAPI,UploadFile
from models.models_actions import load
app = FastAPI()

#charger le model 
model = load()


@app.get("/")
def great():
    return { "message" : "bonjour"}

@app.post("/predict")
def predict(file : UploadFile):
    img = file.read()

    #ouvrir l'image
