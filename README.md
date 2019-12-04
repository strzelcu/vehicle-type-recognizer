# Vehicle type recognizer

## 1. Description

Vehicle type recognizer is a scientific project. The main purpose of this project is to check if there are neural networks helpful in recognizing the vehicle type. I don't give any guarantee that this project will be up to date.

## 2. First stage - acquiring image dataset

To prepare own image dataset I wrote two *bash* scripts to download images from public road cams. Images are publicly available at this [site](https://www.traxelektronik.pl/pogoda/kamery/index.php "traxelektronik"). Images refresh every 5 minutes.

The initial dataset contains around 260000 images of public roads from Poland. Size of this image set is around 37GB. It can be downloaded from this [link](https://www.dropbox.com/sh/tghfefvd7ryqrqt/AADc3hj43PymqG6sC0caFNX1a?dl=0).

To the extent possible under law, I waived all copyright and related or neighboring rights to this vehicle image dataset. This work is published from Poland.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)   

## Development environment prerequisites:

* PyCharm IDE (Recommended)
* Python with version 3.7.3

After cloning of repository you have to [create virtual environment](https://docs.python.org/3.7/library/venv.html "Creation of virtual environments") in project main directory and install all requirements.

1. Run following commands in terminal:
    
    **source venv/bin/activate**
    
    **pip install -r requirements.txt**