import tensorflow as tf
import numpy as np
def load():
    model_path="models/best_model.h5"
    model = tf.keras.models.load_model(model_path,compile=True)
    return model

def preprocess(img):
    print(img.size)
    img = img.resize((224,224))
    print(img.size)
    img = np.asarray(img)
    img = np.expand_dims(img,axis=0)
    return img