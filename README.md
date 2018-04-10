# TrainPredict-Using-Keras

Using Anaconda :

Installation Commands in 'Anaconda Prompt' :

- conda create -n keras pip python=3.5

- activate keras

- pip install --ignore-installed --upgrade tensorflow

- conda install -c conda-forge keras


( Using PIP: pip install keras )

<b> Change Keras Backned: </b>

1. For non Anaconda :

If you are using Anaconda then you will need to set default Backend by editing following file:

- C:\ProgramData\Anaconda3\envs\keras\etc\conda\activate.d\keras_activate.bat

- set "KERAS_BACKEND=tensorflow"

2. For non Anaconda :
Check this file : C:\Users\YourUserName\.keras\keras.json

"image_data_format": "channels_last"

(see <a href="https://keras.io/backend/">Keras Backend <a/> )
  
Open Command Prompt and Set Tensorflow backend

- set "KERAS_BACKEND=tensorflow"


<u> To Change Dir in Ananconda Prompt : </u>

- cd /D D:\Downloads
