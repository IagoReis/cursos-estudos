#!/bin/bash

zip faceanalise.zip faceanalise.py

aws lambda update-function-code --function-name got-face-analise --zip-file fileb://faceanalise.zip