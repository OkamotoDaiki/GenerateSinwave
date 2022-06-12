


# Generate Sin-wave
 
A program that can create a sin wave by specifying the fundamental frequency and time.
 
# DEMO

A sin wave can be generated and a wave file is output.
![sinwave](https://user-images.githubusercontent.com/49944765/173215222-c4968e7a-4955-4ca4-96ec-77af40f3aeff.png)
 
# Features

If you set the output_wave variable to `True`, you can output the generated sin wave file.
 
# Requirement
 
* Python 3.8.10
* numpy 1.21.4
 
# Installation
 
Requirementで列挙したライブラリなどのインストール方法を説明する
 
```python
from generate_sinwave import output_sinwave
f0 = 440
sec = 1
fname = "440Hz.wav"
sin_wave = output_sinwave(f0, sec, output_wave=True, wave_fname=fname)
```
 
# Usage
 
Refer to the `sample.py` program.
 
# Author
 
* Oka.D.
* okamotoschool2018@gmail.com