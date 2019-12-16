#!/bin/bash
# Usage1(production daemon): ./autostartup.sh -d prod
# Usage2(development foreground): ./autostartup.sh

source py3flask/bin/activate
if [ "$1" == '-d' ] || [ "$1" == '--daemon' ]; then
  nohup ./startup.sh "$2" > log.out 2>&1 &
else
  ./startup.sh "$2"
fi
deactivate
