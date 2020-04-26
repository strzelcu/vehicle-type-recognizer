#!/bin/bash

# Script has been prepared for Linux environment e.g. Ubuntu
# Run this script after cloning of the repository in project
# directory. You have to have python3.7 installed.

python3.7 -m venv .venv
source .venv/bin/activate
pip install -r ./project/resources/requirements.txt