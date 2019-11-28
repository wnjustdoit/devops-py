#!/bin/bash

source py3flask/bin/activate
if [ "$1" == '-d' ] || [ "$1" == '--daemon' ]; then
  nohup ./startup.sh > log.out 2>&1 &
  else
    ./startup.sh
fi
deactivate
