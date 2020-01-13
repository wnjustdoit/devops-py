#!/bin/bash

source py3flask/bin/activate
nohup ./startup.sh prod >log.out 2>&1 &
deactivate
