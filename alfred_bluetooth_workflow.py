import json
import subprocess
import sys

from lxml import etree


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
            'type': 'file',
            'arg': _read_string_value(device, 'device_addr'),
            'subtitle': subtitle,
            'connected': is_connected,
            'title': device.xpath('.//key[1]')[0].text,
            'icon': {
                'path': './icons/bluetooth-' + ('connected' if is_connected else 'disconnected') + '.png'
            }
        })

    return bluetooth_devices


if __name__ == '__main__':
    query = sys.argv[1] if len(sys.argv) > 0 else ''

    devices = _read_devices()
    filtered_devices = filter(lambda x: query.strip().lower() in x['title'].lower(), devices)
    print(json.dumps({"items": sorted(filtered_devices, key=lambda d: (not d['connected'], d['title']))}))
