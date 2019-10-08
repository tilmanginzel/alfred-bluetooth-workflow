#!/usr/bin/env bash

PARENT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)
cd "${PARENT_PATH}"

DEVICE=$1
TITLE=$2

if [[ $(../blueutil --is-connected ${DEVICE}) -eq 1 ]]
then
    if [[ $(../blueutil --disconnect ${DEVICE}) -eq 0 ]]
    then
        ./notify.sh -m "Disconnected from ${TITLE}"
    else
        ./notify.sh -m "Failed to disconnect ${TITLE}. Click to retry." -i failure -c "blt.sh ${DEVICE} \"${TITLE}\""
    fi
else
    if [[ $(../blueutil --connect ${DEVICE}) -eq 0 ]]
    then
        ./notify.sh -m "Connected to ${TITLE}" -i success
    else
        ./notify.sh -m "Failed to connect to ${TITLE}. Click to retry." -i failure -c "blt.sh ${DEVICE} \"${TITLE}\""
    fi
fi