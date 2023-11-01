import tensorflow as tf
import numpy as np
def load():
    model_path="best_model.h5"
    model = tf.keras.models.load_model(model_path,compile=False)
    return model

def preprocess(img):
    img = img.resize((224,224))
    img = np.asarray(img)
    img = np.expand_dims(img,axis=0)
    return img