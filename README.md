# TrainPredict-Using-Keras

Using Anaconda :

Installation Commands in 'Anaconda Prompt' :

- conda create -n keras pip python=3.5

- activate keras

- pip install --ignore-installed --upgrade tensorflow

- conda install -c conda-forge keras

- conda install -c menpo opencv


( Using PIP: pip install keras )

<b> Change Keras Backned: </b>

1. For non Anaconda :

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


<u> To Change Dir in Ananconda Prompt : </u>

- cd /D D:\Downloads

==============================================

Result:

--------------

1. train_data_1.py

![console](https://user-images.githubusercontent.com/27011804/38608379-cf95a2ec-3d98-11e8-8f47-ba2e86988fca.PNG)
--------------


![pltresult](https://user-images.githubusercontent.com/27011804/38608394-d9ae79fc-3d98-11e8-8dde-7c1224920e59.jpg)

--------------
