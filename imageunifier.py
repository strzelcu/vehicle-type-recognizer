import argparse
import datetime
import os

import cv2


def read_image(image_path):
    print("[INFO] Reading image {}".format(image_path))
    return cv2.imread(image_path)


def make_square(img):
    print("[INFO] Make square from image")
    height = img.shape[0]
    width = img.shape[1]
    if width > height:
        cut_size = int((width - height) / 2)
        crop_img = img[0:height, cut_size:width - cut_size]
        return crop_img
    else:
        cut_size = int((height - width) / 2)
        crop_img = img[cut_size:height - cut_size, 0:width]
        return crop_img


def resize_image(width, height, img):
    print("[INFO] Resize image to {}x{} pixels".format(width, height))
    dimensions = (width, height)
    return cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)


def save_image(img, filename, path):
    print("[INFO] Saving image {} in path {}".format(filename, path))
    cv2.imwrite(os.path.join(path, filename), img)


def unify_images(path, class_name, size):
    counter = 1
    target_directory = "/processed-{}-{}x{}px".format(class_name, size, size)
    if not os.path.exists(path + target_directory):
        print("[INFO] ## Creating target directory".format(target_directory))
        os.mkdir(path + target_directory)
    for file in os.listdir(path):
        try:
            filename = class_name + str(counter) + ".png"
            print("[INFO] ### Processing file {}".format(file))
            img = read_image(path + "/" + file)
            img = make_square(img)
            img = resize_image(size, size, img)
            save_image(img, filename, path + target_directory)
            counter += 1
        except AttributeError as error:
            print(error)


# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument("-c", "--class", required=True, help="image class name")
ap.add_argument("-s", "--size", type=int, default=32, help="# width and height of result images")
args = vars(ap.parse_args())

print("[INFO] Start of processing at {}".format(datetime.datetime.now()))
unify_images(args["dataset"], args["class"], args["size"])
print("[INFO] Finish of processing at {}".format(datetime.datetime.now()))
