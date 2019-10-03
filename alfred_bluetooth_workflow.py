import subprocess
import sys

from lxml import etree
from workflow import Workflow3

log = None
GITHUB_SLUG = 'tilmanginzel/alfred-bluetooth-workflow'


def _find_element_by_key(device, key):
    elements = device.xpath(".//*[text()='{}']/following-sibling::string[1]".format(key))
    return elements[0] if len(elements) else None


def _read_string_value(device, key):
    elem = _find_element_by_key(device, key)
    return elem.text if elem is not None else None


def _read_boolean_value(device, key):
    elem = _find_element_by_key(device, key)
    return True if elem is not None and elem.text == 'attrib_Yes' else False


def _read_devices():
    proc = subprocess.Popen(['system_profiler', 'SPBluetoothDataType', '-xml'], stdout=subprocess.PIPE)
    bluetooth_devices_xml_raw = proc.stdout.read()
    bluetooth_devices_xml = etree.fromstring(bluetooth_devices_xml_raw).xpath("//*[text()='device_title']/following-sibling::array[1]/dict")

    bluetooth_devices = []

    for device in bluetooth_devices_xml:
        is_connected = _read_boolean_value(device, 'device_isconnected')
        battery = _read_string_value(device, 'device_batteryPercent')
        subtitle = ('Connected' if is_connected else 'Disconnected') + (', ' + battery if battery else '')

        bluetooth_devices.append({
            'type': 'file:skipcheck',
            'arg': _read_string_value(device, 'device_addr'),
            'subtitle': subtitle,
            'connected': is_connected,
            'title': device.xpath('.//key[1]')[0].text,
            'icon': './icons/bluetooth-' + ('connected' if is_connected else 'disconnected') + '.png'
        })

    return bluetooth_devices


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
