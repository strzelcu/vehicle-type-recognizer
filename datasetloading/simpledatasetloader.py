import os

import cv2
import numpy as np


class SimpleDatasetLoader:
    def __init__(self, preprocessors=None):
        # Store the image preprocessor if needed
        self.preprocessors = preprocessors

        # If the preprocessors are None, initialize them as an empty list
        if self.preprocessors is None:
            self.preprocessors = []

    def load(self, image_paths, verbose=-1):
        # Initialize the list of features and labels
        data = []
        labels = []

        # Loop over the input images
        for (i, imagePath) in enumerate(image_paths):
            # Load the image and extract the class label assuming
            # that our path has the following format:
            # /path/to/dataset/{class}/{image}.jpg
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]

            # Check to see if our preprocessors are not None
            if self.preprocessors is not None:
                # Loop over the preprocessors and apply each to the image
                for p in self.preprocessors:
                    image = p.preprocess(image)

            # Treat our processed image as a "feature vector"
            # by updating the data list followed by the labels
            data.append(image)
            labels.append(label)

            # Show an update every 'verbose' images
            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print("[INFO] processed {}/{}".format(i + 1, len(image_paths)))

        # Return a tuble of the data and labels
        return np.array(data), np.array(labels)
