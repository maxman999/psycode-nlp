#!/bin/bash

REPOSITORY=/home/ec2-user/app/psycode-nlp
APPLICATION_NAME=nlp_app.py


echo " > 현재 구동중인 플라스크 중지"
fuser -k -n tcp 5000

echo " > activate venv"
. ~/.venv/bin/activate

echo " > run flask"
nohup python3 -u $REPOSITORY/$APPLICATION_NAME &

