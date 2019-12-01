#!/bin/bash

# Script responsible for change filenames to unify all names of images in database

# Path to iteration
path=$1
# Iteration number
iteration=$2

for filename in $path/*; do
	mv "$filename" "$path/it$2-$iteration.jpg" 
	((iteration++))
done
