#!/usr/bin/env bash

PARENT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)
cd "${PARENT_PATH}"

../blueutil -p toggle

if [[ $(../blueutil -p) -eq 1 ]]
then
    ./notify.sh -m "Bluetooth turned on" -i success
else
    ./notify.sh -m "Bluetooth turned off"
fi