# =========================== Part 2: Prediction ===========================
testImageFolder = "data\\predict\\1120"

import numpy as np
from sys import argv
import os,cv2, random
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import matplotlib.pyplot as plt

# --------- Define Input Parameters ---------
img_width, img_height = 150, 150
#var_test_image = argv[1]
# --------- ----------------------- ---------

def get_image(path):
    img = image.load_img(path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x



def load_images_from_folder(folder):
	images = []	
	
	for filename in os.listdir(folder):
		imgRead = os.path.join(folder,filename)
		if imgRead is not None:							
			img = image.load_img(imgRead, target_size=(img_width, img_height))
			x = image.img_to_array(img)			
			model = load_model("data/d0/output/50epoch3h/Model.h5")
			# -------------------- Predictions ------------------------ 			
			accuracy = model.predict(np.expand_dims(x, axis=0))
			print("-----------------------------------------")					
			print("Prediction Accuracy = " + str(accuracy))
			classes = model.predict_classes(np.expand_dims(x, axis=0))			
			print("Prediction Class = {} ".format(classes))
			if classes == 1:      
				print(imgRead + ' ---> This is a Dog')
			else:
				print(imgRead + ' ---> This is a Cat')			
	return images
	

images  = load_images_from_folder(testImageFolder)

print("-----------------------------------------")			
# ----------------------------------------------------------------
