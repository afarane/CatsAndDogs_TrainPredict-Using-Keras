from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from keras import backend as K
import matplotlib.pyplot as plt

# ---------Define Input Parameters--------------------------------
img_width, img_height = 300, 300

# ---------Define Backend-----------------------------------------
# if channels_first then Theano , if channels_last then TensorFlow

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# ==========Model Architecture====================================
# Imput Layer 
model = Sequential()

model.add(Conv2D(32, (3, 3), padding="same", input_shape=input_shape,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# Layer 1
model.add(Conv2D(32, (3, 3), padding="same",activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.2))

# Layer 2
model.add(Conv2D(64, (3, 3), padding="same",activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.2))

# Flattening 
model.add(Flatten())

# Full Connection
model.add(Dense(units = 64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=64,activation='relu'))
model.add(Dropout(0.2))

# Output Layer
model.add(Dense(units=1, activation='sigmoid'))

# Compiling the CNN
model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])


# ================ data augmentation
from keras.preprocessing.image import ImageDataGenerator
	
batch_size = 5

# 0. Prepare data augmentation configuration
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./ 255)

# 1. Training Set 
train_data_dir = 'data/train_data'
training_set = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# 2. Test Set 	
test_data_dir = 'data/test_data'
test_set = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# 3. Create a loss history
train_samples = 7
test_samples = 5
epoch = 10
history  = model.fit_generator(
    training_set,
    steps_per_epoch=train_samples, 
    epochs=epoch, 
    validation_data=test_set, 
    validation_steps=test_samples )
	

# ======================== Save Model==============================
#model.save_weights("output/Model_weights.h5")
model.save("data/output/Model.h5",True)
print("Saved model to disk")

#  "Accuracy"
print(history.history.keys())
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.savefig("data/output/PLTResult.jpg")
print("Saved model to disk")
plt.show()

# ----------------------------------------------------------------
print('Training Finished ! ')

# ========================= Part 2: Prediction =============================
var_test_image = 'data/predict/d2.png'

import numpy as np
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
