from pathlib import Path
import numpy as np
import cv2
from keras.models import load_model
from datetime import datetime

print("loading model")
now = datetime.now()
model = load_model("./models/20190128103330_0.3/cableclassifier_20190128103330_0.3.h5")
time_delta = now - datetime.now()
print("model loaded in {} milliseconds".format(time_delta.microseconds))
img_arrays = []
filenames = []
print("loading images")
for img in Path("./data/utp/").iterdir():
    img_arrays.append(cv2.imread(str(img)))
    filenames.append(str(img.name))
img_arrays = np.array(img_arrays)
print("predict images")
for i in range(1000):
    for i in range(len(img_arrays)):
        now = datetime.now()
        print('Prediction for image {}: {}'.format(filenames[i], model.predict(np.expand_dims(img_arrays[i], axis=0))))
        time_delta = now - datetime.now()
        print('It took {} milliseconds'.format(time_delta.microseconds))
