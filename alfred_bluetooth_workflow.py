import subprocess
import sys
import json

from workflow import Workflow3

log = None
GITHUB_SLUG = 'tilmanginzel/alfred-bluetooth-workflow'


def _read_devices():
    proc = subprocess.Popen(['./blueutil', '--paired', '--format=JSON'], stdout=subprocess.PIPE)

    devices_raw = json.loads(proc.stdout.read())
    bluetooth_devices = []

    for device in devices_raw:
        if device['name'] and device['address'] and device['connected'] is not None:
            is_connected = device['connected']

            bluetooth_devices.append({
                'type': 'file:skipcheck',
                'arg': device['address'],
                'subtitle': 'Connected' if is_connected else 'Disconnected',
                'connected': is_connected,
                'title': device['name'],
                'icon': './icons/bluetooth-' + ('connected' if is_connected else 'disconnected') + '.png'
            })

    return sorted(bluetooth_devices, key = lambda x: (-x['connected'], x['title']))


def main(wf):
    if wf.update_available:
        wf.add_item('Update available for Bluetooth Connector!',
                    autocomplete='workflow:update',
                    valid=False)

    query = wf.args[0] if len(wf.args) else None
    devices = _read_devices()

    filtered_devices = wf.filter(query, devices, key=lambda k: k['title'])

    for device in filtered_devices:
        item = wf.add_item(
            type=device['type'],
            title=device['title'],
            subtitle=device['subtitle'],
            arg=device['arg'],
            icon=device['icon'],
            valid=True
        )

        item.setvar('title', device['title'])

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3(update_settings={'github_slug': GITHUB_SLUG})
    log = wf.logger
    sys.exit(wf.run(main))
