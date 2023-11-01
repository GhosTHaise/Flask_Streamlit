import tensorflow as tf
def load():
    model_path="best_model.h5"
    model = tf.keras.models.load_model(model_path,compile=False)
    return model