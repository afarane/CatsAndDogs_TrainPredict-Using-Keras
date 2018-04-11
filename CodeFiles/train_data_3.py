from keras.models import Sequential
#from keras import optimizers
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from keras import backend as K
import matplotlib.pyplot as plt

# --------- Define Input Parameters ---------
img_width, img_height = 150, 150
# ----
train_data_dir = 'train4k'
validation_data_dir = 'validation0.8k'
# ----
nb_train_samples = 4000
nb_validation_samples = 800
batch_size = 100
epoch = 50

# ----

# --------- Define Backend ---------
# if channels_first then Theano , if channels_last then TensorFlow

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# =========================== Model Architecture ===========================
# Imput Layer 
model = Sequential()

model.add(Conv2D(32, (3, 3), padding="same", input_shape=input_shape,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


# Layer 1
model.add(Conv2D(8, (3, 3), padding="same",activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

# Layer 2
model.add(Conv2D(16, (3, 3), padding="same",activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

# Layer 3
model.add(Conv2D(32, (3, 3), padding="same",activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

# Layer 4
model.add(Conv2D(64, (3, 3), padding="same",activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

# Flattening 
model.add(Flatten())

# Full Connection
model.add(Dense(units=64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=64,activation='relu'))
model.add(Dense(units=64,activation='relu'))
model.add(Dropout(0.2))


# Final / Output Layer
model.add(Dense(units=1, activation='sigmoid'))

# Compiling the CNN
model.compile(optimizer='nadam',loss='binary_crossentropy', metrics=['accuracy'])


# --------- data augmentation ---------
from keras.preprocessing.image import ImageDataGenerator


# 0. Prepare data augmentation configuration
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

validation_datagen = ImageDataGenerator(rescale=1./ 255)

# 1. Training Set 
training_set = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# 2. Validation Set 	
validation_set = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# 3. Create a loss history

history  = model.fit_generator(
    training_set,
    steps_per_epoch=nb_train_samples // batch_size, # // batch_size
    epochs=epoch,
	verbose=2,
	validation_data=validation_set,
    validation_steps=nb_validation_samples // batch_size) # // batch_size
	


# ======================== Save Model ==============================
#model.save_weights("output/Model_weights.h5")
model.save("output/Model.h5",True)
print("Saved model to disk")

print("validation_set class_indices = {} ".format(validation_set.class_indices))

#  "Accuracy"
print(history.history.keys())
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.savefig("output/PLTResult.jpg")
print("Saved model to disk")
#plt.show()

# ----------------------------------------------------------------
print('Training Finished ! ')
# ----------------------------------------------------------------
