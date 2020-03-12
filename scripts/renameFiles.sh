#!/bin/bash

# Script responsible for change filenames to unify all names of images in dataset

# Example usage:
#   ./renameFiles.sh ../dataset/vehicles/car car

# Path of images directory
path=$1
# Class of image
class=$2
# Iteration number
it=1
# Target directory
targetDir="renamed"

# Create target directory
if [[ ! -e ${path}/../${targetDir} ]]; then
    mkdir ${path}/../${targetDir}
fi

for filename in $path/*; do
    echo "Copying file $filename to $path/$targetDir"
	cp "$filename" "$path/../$targetDir/$class$it.jpg"
	((it++))
done
