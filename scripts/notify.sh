#!/usr/bin/env bash

>&2 echo "[debug] ./notify script triggered"

PARENT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)
cd ${PARENT_PATH}

while getopts ":m:i:" opt; do
    case ${opt} in
        m) MESSAGE="$OPTARG"
        ;;
        i) ICON="$OPTARG"
        ;;
    esac
done

CONTENT_IMAGE_OPT=""
if ! [[ -z ${ICON} ]]
then
    CONTENT_IMAGE_OPT="-contentImage ../icons/${ICON}.png"
fi

>&2 echo "[debug] Send notification (message: ${MESSAGE}, image: ${CONTENT_IMAGE_OPT})"

../terminal-notifier.app/Contents/MacOS/terminal-notifier \
    -title "Bluetooth" \
    -sender "de.tilmanginzel.alfred.bluetooth" \
    -message "${MESSAGE}" \
    ${CONTENT_IMAGE_OPT}

>&2 echo "[debug] Notification sent successfully"
