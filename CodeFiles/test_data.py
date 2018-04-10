# =========================== Part 2: Prediction ===========================
var_test_image = 'data/predict/d2.png'

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from matplotlib.pyplot import imshow


def get_image(path):
    img = image.load_img(path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x
 
img, x = get_image(var_test_image)    
#model = load_model("data/output/Model.h5")
result= model.predict(x)
imshow(img)
 
training_set.class_indices

# Result
result[0][0]
if result[0][0] ==1:
    prediction = 'File01'
    print("prediction = " + prediction)
else:
    prediction = 'File02'
    print("prediction = " + prediction)
    

# ----------------------------------------------------------------
