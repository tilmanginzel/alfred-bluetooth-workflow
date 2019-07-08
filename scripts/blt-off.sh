#!/usr/bin/env bash

PARENT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)
cd "${PARENT_PATH}"

../blueutil -p 0

if [[ $(../blueutil -p) -eq 0 ]]
then
    ./notify.sh -m "Bluetooth turned off"
else
    ./notify.sh -m "Failed to turn Bluetooth off. Click to retry." -i failure -c "blt-off.sh"
fi