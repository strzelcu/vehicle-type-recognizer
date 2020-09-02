import argparse
import datetime
import os
import sys
from configparser import RawConfigParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from imutils import paths
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

score_rate = [0.576, 0.556, 0.5816, 0.5584, 0.56, 0.5632, 0.548, 0.54, 0.536, 0.556, 0.5472, 0.5456, 0.5376, 0.5456, 0.5432, 0.5416, 0.5456, 0.54, 0.5288, 0.5312]
error_rate = [0.424, 0.444, 0.4184, 0.4416, 0.44, 0.4368, 0.452, 0.46, 0.464, 0.444, 0.4528, 0.4544, 0.4624, 0.4544, 0.4568, 0.4584, 0.4544, 0.46, 0.4712, 0.4688]

plt.figure(figsize=(10, 6))
plt.plot(range(0, 20), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.xticks(range(0, 20))
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(range(0, 20), score_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.xticks(range(0, 20))
plt.title('Score Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Score Rate')
plt.show()

print("[INFO] Finish of processing at {}".format(datetime.datetime.now()))
