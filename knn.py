import argparse
import os
import sys
import datetime

from pathlib import Path
from configparser import RawConfigParser
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths

sys.path.insert(0, os.getcwd())
from preprocessing.simplepreprocessor import SimplePreprocessor
from datasetloading.simpledatasetloader import SimpleDatasetLoader

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1, help="# of nearest neighbors for classification")
ap.add_argument("-j", "--jobs", type=int, default=-1, help="# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

# Parse config file
config = RawConfigParser()
properties_file = Path("resources/project.properties")
if not properties_file.exists():
    properties_file = Path("resources/default.properties")
config.read(properties_file.absolute(), encoding="utf-8")

# Prepare variables
verbose_checkpoint = int(config.get("ImageDatasetLoad", "image.verbose"))
image_size = int(config.get("ImagePreprocess", "image.size"))

# Grab the list of images that we'll be describing
print("[INFO] Start of processing at {}".format(datetime.datetime.now()))
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))

# Initialize the image preprocessor, load the dataset from disk and reshape the data matrix
sp = SimplePreprocessor(image_size, image_size)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose=verbose_checkpoint)
data = data.reshape((data.shape[0], (image_size * image_size * 3)))

# Show some information on memory consumption of the images
print("[INFO] features matrix: {:.1f}MB".format(data.nbytes / (1024 * 1000.0)))

# Encode the labels as integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# Partition the data into training and testing splits using 75%
# of the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25, random_state=42)

# Train and evaluate a k-NN classifier on the raw pixel intensities
print("[INFO] evaluating k-NN classifier...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"], n_jobs=args["jobs"])
model.fit(trainX, trainY)
print(classification_report(testY, model.predict(testX), target_names=le.classes_))
print("[INFO] Finish of processing at {}".format(datetime.datetime.now()))
