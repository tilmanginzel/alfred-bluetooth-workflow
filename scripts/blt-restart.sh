#!/usr/bin/env bash

PARENT_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)
cd "${PARENT_PATH}"

./blt-off.sh

# Sleep is not strictly necessary, but gives a nice user experience as you can
# visually see the Bluetooth be turned off and then on again in the icon and
# notifications.
sleep 0.5

./blt-on.sh
