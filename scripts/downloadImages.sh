#!/bin/bash

# This script downloads all *.jpg files from sites in prepared file.
# Parameters:
#   1. File with url list
#   2. Number of first iteration
#   3. Number of last iteration

# Example usage:
#   ./downloadImages.sh urls/finalUrlList 51 60
#   nohup ./downloadImages.sh urls/finalUrlList 51 60

#   To get log from script just run it with nohup

fileWithUrlList=$1
listOfUrls=$(cat ${fileWithUrlList});
iteration=$2
targetDir="target"
logFile="$targetDir/run.log"
datePattern="+%F-%T.%N"

# Create target directory
if [[ ! -e ${targetDir} ]]; then
    mkdir ${targetDir}
fi

# Create log file
if [[ ! -e ${logFile} ]]; then
	touch ${logFile}
fi

while [[ ${iteration} -le $3 ]]; do
	imageNumber=1
	echo "$(date ${datePattern}): Iteration $iteration has been started." >> ${logFile}
	for line in ${listOfUrls}; do
		url=${line}
		request="$url"
		response=$(curl -s "$url")
		imageUrls=$(grep -oP 'http.?://\S+jpg' <<< "$response")
		if [[ ! -d iteration${iteration} ]]; then
			mkdir -p ./target/iteration${iteration}
		fi
		for line in ${imageUrls}; do
			$(wget ${line} -O ./target/iteration${iteration}/it${iteration}-${imageNumber}.jpg)
			echo "$(date ${datePattern}): Image $line has been downloaded." >> ${logFile}
			((imageNumber++))
		done
	done
	echo "$(date ${datePattern}): Iteration $iteration has been finished." >> ${logFile}
	((iteration++))
	sleep 30s
done
echo "$(date ${datePattern}): All iterations has been finished." >> ${logFile}
