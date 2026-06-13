import tensorflow as tf

def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(224, 224, 3)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(4, activation="softmax")
    ])
    return model
