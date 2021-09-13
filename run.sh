#!/bin/bash
pip install -r requirements.txt
if [ ! -f parking_citations.corrupted.csv ]
then
    curl -O https://s3-us-west-2.amazonaws.com/pcadsassessment/parking_citations.corrupted.csv
else
    echo "File found"
fi
python run.py
