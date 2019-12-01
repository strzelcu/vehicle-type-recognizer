# Vehicle type recognizer

## 1. Description

Vehicle type recognizer is a scientific project. The main purpose of this project is to check if there are neural networks helpful in recognizing the vehicle type.

## 2. First stage - acquiring image database

To prepare own image database I wrote two *bash* scripts to download images from public road cams. Images are publicly available at this [site](https://www.traxelektronik.pl/pogoda/kamery/index.php "traxelektronik"). Images refresh every 5 minutes.

## Development environment prerequisites:

* PyCharm IDE (Recommended)
* Python with version 3.7.3

After cloning of repository you have to [create virtual environment](https://docs.python.org/3.7/library/venv.html "Creation of virtual environments") in project main directory and install all requirements.

1. Run following commands in terminal:
    
    **source venv/bin/activate**
    
    **pip install -r requirements.txt**