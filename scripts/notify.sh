#!/usr/bin/env bash

>&2 echo "[debug] ./notify script triggered"

PARENT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)
cd "${PARENT_PATH}"

while getopts ":m:i:c:" opt; do
    case ${opt} in
        m) MESSAGE="$OPTARG"
        ;;
        i) ICON="$OPTARG"
        ;;
        c) COMMAND="$OPTARG"
        ;;
    esac
done

CONTENT_IMAGE_OPT=""
if ! [[ -z ${ICON} ]]
then
    CONTENT_IMAGE_OPT="-contentImage ../icons/${ICON}.png"
fi

COMMAND_OPT=""
if ! [[ -z ${COMMAND} ]]
then
    # command path must be escaped with '\ ' instead of quotes ""
    ESCAPED_PARENT_PATH=$(echo "${PARENT_PATH}" | sed 's/ /\\ /g')
    COMMAND_OPT="${ESCAPED_PARENT_PATH}/$COMMAND"
fi

>&2 echo "[debug] Send notification (message: ${MESSAGE}, image: ${CONTENT_IMAGE_OPT}, command: ${COMMAND_OPT})"

if ! [[ -z ${COMMAND_OPT} ]]
then
    # do not specify -sender as this breaks the -execute command
    ../terminal-notifier.app/Contents/MacOS/terminal-notifier \
        -title "Bluetooth" \
        -message "${MESSAGE}" \
        -appIcon "${PARENT_PATH}/../icon.png" \
        -execute "${COMMAND_OPT}" \
        ${CONTENT_IMAGE_OPT}
else
    ../terminal-notifier.app/Contents/MacOS/terminal-notifier \
        -title "Bluetooth" \
        -appIcon "${PARENT_PATH}/../icon.png" \
        -message "${MESSAGE}" \
        ${CONTENT_IMAGE_OPT}
fi

>&2 echo "[debug] Notification sent successfully"
