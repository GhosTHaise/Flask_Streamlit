from fastapi import FastAPI,UploadFile
from models.models_actions import load, preprocess
import io
from PIL import Image

app = FastAPI()

#charger le model 
model = load()


@app.get("/")
def great():
    return { "message" : "bonjour"}

@app.post("/predict")
async def predict(file : UploadFile):
    img_data = await  file.read()

    #ouvrir l'image
    img = Image.open(io.BytesIO(img_data)) 

    #preprocessing
    img_processed = preprocess(img)

    # predictions

    pred = model.predict(img_processed)
    rec = pred[0][0].tolist()
    print(pred)
    return {
        "predictions" : rec
    }