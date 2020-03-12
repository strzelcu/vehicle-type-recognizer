#!/bin/bash

# This script scans range of $url from $lowerLimit to $upperLimit.
# If site html code contains *.jpg images then $url is added to the grabbedUrlList file

# Example usage:
#   ./grabUrlList.sh 1 20000

lowerLimit=$1;
upperLimit=$2;
targetDir="urls"
url="https://www.traxelektronik.pl/pogoda/kamery/kamera.php?pkamnum=";
grabbedUrlListFile="$targetDir/grabbedUrlList";

# Create target directory
if [[ ! -e ${targetDir} ]]; then
    mkdir ${targetDir}
fi

for (( i=$lowerLimit; i<=$upperLimit; i++ )) do
	request="$url$i";
	response=$(curl -s "$url$i");
	imageUrls=$(grep -oP 'http.?://\S+jpg' <<< "$response");
	if [[ -n $imageUrls ]]; then
		echo $request >> ${grabbedUrlListFile}
	fi
done