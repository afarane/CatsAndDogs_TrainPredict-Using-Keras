# =========================== Part 2: Prediction ===========================
var_test_image = 'data/predict/4.jpg'

import numpy as np
import os, cv2, random
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import matplotlib.pyplot as plt

# --------- Define Input Parameters ---------
img_width, img_height = 150, 150

def get_image(path):
    img = image.load_img(path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x
 

img, x = get_image(var_test_image)    
model = load_model("data/output/Model.h5")
predictions= model.predict(x)
plt.imshow(img)
#plt.show()	

# Result

predictions[0][0]
if predictions[0][0] == 0:      
	print('I think this is a Cat')
else:
    print('I think this is a Dog')


# ----------------------------------------------------------------
