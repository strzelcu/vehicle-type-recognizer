import argparse
import datetime
import itertools

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.constraints import max_norm
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="# path to input dataset")
ap.add_argument("-s", "--size", type=int, default=32, help="# width and height of result images")
ap.add_argument("-e", "--epochs", type=int, default=25, help="# amount of training steps")
ap.add_argument("-b", "--batch", type=int, default=64, help="# batch size for training steps")
ap.add_argument("-v", "--validation", type=int, default=50, help="# validation steps")
args = vars(ap.parse_args())

print("[INFO] {} Start of processing".format(datetime.datetime.now()))

TRAINING_DATA_DIR = str(args["dataset"])
IMAGE_SIZE = args["size"]
IMAGE_SHAPE = (args["size"], args["size"])
EPOCHS = args["epochs"]
BATCH_SIZE = args["batch"]
VALIDATION_STEPS = args["validation"]
print("[INFO] {} Image shape size is {}".format(datetime.datetime.now(), IMAGE_SHAPE))
print("[INFO] {} Image dataset directory is {}".format(datetime.datetime.now(), TRAINING_DATA_DIR))

# Set random seed for purposes of reproducibility
seed = 21

# Prepare keyword arguments of training dataset
datagen_kwargs = dict(rescale=1. / 255, validation_split=.20)

# Prepare validation data
test_datagen = keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
test_generator = test_datagen.flow_from_directory(
    TRAINING_DATA_DIR,
    subset="validation",
    shuffle=True,
    target_size=IMAGE_SHAPE
)

# Prepare training data
train_datagen = keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
train_generator = train_datagen.flow_from_directory(
    TRAINING_DATA_DIR,
    subset="training",
    shuffle=True,
    target_size=IMAGE_SHAPE
)

labels = "\n".join(sorted(train_generator.class_indices.keys()))
with open("target/labels.txt", "w") as f:
    f.write(labels)
print("[INFO] {} Found labels: \n\t {}".format(datetime.datetime.now(), train_generator.class_indices))

NUM_CLASSES = train_generator.num_classes

print("[INFO] {} Creating pre-trained model".format(datetime.datetime.now()))
model = Sequential()

model.add(Conv2D(150, (3, 3), input_shape=train_generator.image_shape, padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dropout(0.2))

model.add(Dense(256, kernel_constraint=max_norm(3)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(128, kernel_constraint=max_norm(3)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(NUM_CLASSES))
model.add(Activation('softmax'))

model.build([None, 150, 150, 3])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

np.random.seed(seed)
hist = model.fit(train_generator, validation_data=test_generator, epochs=EPOCHS, batch_size=BATCH_SIZE).history

print("[INFO] {} Finish of model creation".format(datetime.datetime.now()))

scores = model.evaluate(test_generator, verbose=1)
final_loss, final_accuracy = model.evaluate(test_generator, steps=VALIDATION_STEPS)

print("[INFO] {} Model accuracy: {}".format(datetime.datetime.now(), scores[1] * 100))
print("[INFO] {} Model loss: {}".format(datetime.datetime.now(), scores[0]))

# Draw LOSS figure
plt.figure()
plt.ylabel("Loss (training and validation)")
plt.xlabel("Training Steps")
plt.ylim([0, 50])
plt.plot(hist["loss"])
plt.plot(hist["val_loss"])
plt.show()

# Draw ACC figure
plt.figure()
plt.ylabel("Accuracy (training and validation)")
plt.xlabel("Training Steps")
plt.ylim([0, 1])
plt.plot(hist["accuracy"])
plt.plot(hist["val_accuracy"])
plt.show()

# Draw figure with partial model predictions
val_image_batch, val_label_batch = next(iter(test_generator))
true_label_ids = np.argmax(val_label_batch, axis=-1)
tf_model_predictions = model.predict(val_image_batch)
dataset_labels = sorted(train_generator.class_indices.items(), key=lambda pair: pair[1])
dataset_labels = np.array([key.title() for key, value in dataset_labels])
predicted_ids = np.argmax(tf_model_predictions, axis=-1)
predicted_labels = dataset_labels[predicted_ids]

plt.figure(figsize=(10, 9))
plt.subplots_adjust(hspace=0.5)
for n in range((len(predicted_labels) - 2)):
    plt.subplot(6, 5, n + 1)
    plt.imshow(val_image_batch[n])
    color = "green" if predicted_ids[n] == true_label_ids[n] else "red"
    plt.title(predicted_labels[n].title(), color=color)
    plt.axis("off")
    _ = plt.suptitle("Model predictions (green: correct, red: incorrect)")
plt.show()

# Draw confusion matrix for model predictions
test_generator.batch_size = 1000
final_test_image_batch, final_test_label_batch = next(iter(test_generator))
final_model_predictions = model.predict(final_test_image_batch)
final_true_test_label_ids = np.argmax(final_test_label_batch, axis=-1)
final_predicted_ids = np.argmax(final_model_predictions, axis=-1)
cm = confusion_matrix(final_true_test_label_ids, final_predicted_ids)
classes = train_generator.class_indices.keys()
print(cm)
plt.imshow(cm, interpolation='nearest', cmap='viridis')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)
thresh = cm.max() / 2.
for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, cm[i, j],
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black")

plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

print("[INFO] {} Finish of processing at {}".format(datetime.datetime.now(), datetime.datetime.now()))
