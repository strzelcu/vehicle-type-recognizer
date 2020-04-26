# Vehicle type recognizer

## 1. Description

Vehicle type recognizer is a scientific project. The main purpose of this project is to check if there are neural networks helpful in recognizing the vehicle type. Project has been prepared and implemented using Linux environment. To init project after cloning just run script *init_project.sh*.

## 2. First stage - acquiring image dataset
To prepare own image dataset I wrote two *bash* scripts to download images from public road cams. Images are publicly available at this [site](https://www.traxelektronik.pl/pogoda/kamery/index.php "traxelektronik"). Images refresh every 5 minutes.

The initial dataset contains around 260000 images of public roads from Poland. Size of this image set is around 37GB. It can be downloaded from this [link](https://www.dropbox.com/sh/tghfefvd7ryqrqt/AADc3hj43PymqG6sC0caFNX1a?dl=0).

To the extent possible under law, I waived all copyright and related or neighboring rights to this vehicle image dataset.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)   

## 3. Second stage - dataset images selecting and unifying

To adjust vehicle types image dataset an image unifier has been implemented. I manually choose and prepare a thousand images for each vehicle type. Image size and name has been unified using *imageunifier.py*

Vehicle types image set can be downloaded from this [link](https://www.dropbox.com/sh/9u7jh7pfrh3wnof/AAA3ATBt2o4z0YrH5A_ofrKSa?dl=0).

To the extent possible under law, I waived all copyright and related or neighboring rights to this vehicle types dataset.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/) 

## 4. Third stage - dataset preprocessing

## 5. Fourth stage - Implementation of neural network algorithms

    * python knn.py --dataset resources/vehicles
