# CatsAndDogs_TrainPredict-Using-Keras

<b>Dataset :</b>

<a href=""https://www.kaggle.com/c/dogs-vs-cats/data>kaggle</a>

</b> Installations : </b>

<u> Using Anaconda :</u>

Installation Commands in 'Anaconda Prompt' :

- conda create -n keras pip python=3.5

- activate keras

- pip install --ignore-installed --upgrade tensorflow

- conda install -c conda-forge keras

- conda install -c menpo opencv


( Using PIP: pip install keras )

--------------------

<b><u> Change Keras Backned: </b></u>

1. For Anaconda :

If you are using Anaconda then you will need to set default Backend by editing following file:

- ${CONDA_PREFIX}/etc/conda/activate.d/keras_activate.bat

(Ex. C:\ProgramData\Anaconda3\envs\keras\etc\conda\activate.d\keras_activate.bat )

- set "KERAS_BACKEND=tensorflow"


2. For non Anaconda :

Check this file : C:\Users\YourUserName\.keras\keras.json

"image_data_format": "channels_last"

(see <a href="https://keras.io/backend/">Keras Backend <a/> )
  
Open Command Prompt and Set Tensorflow backend

- set "KERAS_BACKEND=tensorflow"


<u> Tip: To Change Dir in Ananconda Prompt : </u>

- cd /D D:\Downloads

==============================================

# Results:

--------------

<b> 1. train_data_1 </b>

Optimizer = adam | Hidden_Layers = 2 | epoch = 50 | Final val_acc = 81.13%

nb_train_samples = 4000

nb_validation_samples = 800

Console Output :

![console](https://user-images.githubusercontent.com/27011804/38608379-cf95a2ec-3d98-11e8-8f47-ba2e86988fca.PNG)

PLT Result :

![pltresult](https://user-images.githubusercontent.com/27011804/38608394-d9ae79fc-3d98-11e8-8dde-7c1224920e59.jpg)

--------------
<b> 2. train_data_2 </b>

nb_train_samples = 4000

nb_validation_samples = 800

Optimizer = rmsprop | Hidden_Layers = 3 | epoch = 50 | Final val_acc = 83.25%

Console Output :

![train_data_2](https://user-images.githubusercontent.com/27011804/38619298-7cd4163a-3db9-11e8-9255-01139c277381.PNG)

PLT Result :

![pltresult](https://user-images.githubusercontent.com/27011804/38619248-5e588790-3db9-11e8-94f8-9f2aa8b50b74.jpg)


--------------
<b> 3. train_data_3 </b>

Optimizer = adam | Hidden_Layers = 3 | epoch = 60 | Final val_acc = 86.87%

nb_train_samples = 4000

nb_validation_samples = 800

Console Output :

![capture](https://user-images.githubusercontent.com/27011804/38685259-1a12ed2e-3e8f-11e8-85de-f2cb5354ebc9.PNG)

PLT Result :

![pltresult](https://user-images.githubusercontent.com/27011804/38685244-11b3dea4-3e8f-11e8-8039-0327f57bda34.jpg)


--------------

<b> 4. train_data_4 </b>

Optimizer = adam | Hidden_Layers = 4 | epoch = 50 | Final val_acc = 91.80%

nb_train_samples = 10000

nb_validation_samples = 3000

Console Output :

![capture](https://user-images.githubusercontent.com/27011804/38733984-96c665fa-3f41-11e8-98e9-b2ca794f949f.PNG)

PLT Result :

![pltresult](https://user-images.githubusercontent.com/27011804/38733987-9827152a-3f41-11e8-87b1-448738a4fad8.jpg)


--------------
