import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf

from keras.models import load_model

model = load_model('/home/filter/keras_model')

print("hu")
print(model)
