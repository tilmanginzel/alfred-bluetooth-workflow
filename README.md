# Alfred Bluetooth Workflow

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[Alfred 3](https://www.alfredapp.com/) workflow to quickly connect / disconnect Bluetooth devices.

## Installation

Simply download the latest [`Bluetooth Connector.alfredworkflow`](https://github.com/tilmanginzel/alfred-bluetooth-workflow/releases)
 release and double-click to import into Alfred. 

## Features

* Connect / disconnect to any known Bluetooth device by typing `blt {device}`
  * Optionally filter devices by name
  * Already connected devices are highlighted with a green icon
  * Battery percentage is shown if available
* Power Bluetooth on or off via `blt-on`, `blt-off` or simply toggle via `blt-t`
* Workflow updates via `blt workflow:update` (Thanks to @trietsch)

<img src="./preview1.jpg" width="600" alt="Preview: Alfred Bluetooth Workflow" />
<img src="./preview2.jpg" width="600" alt="Preview: Alfred Bluetooth Workflow" />

## Attribution

* [trietsch/alfred-bluetooth-connector](https://github.com/trietsch/alfred-bluetooth-connector) by Robin Trietsch was used as an inspiration for this workflow implementation
* [toy/blueutil](https://github.com/toy/blueutil) is used to easily connect/disconnect a Bluetooth device by its MAC address and toggle Bluetooth on/off. It was originally developed by Frederik Seiffert and is now being continued by Ivan Kuchin.

## License

```
The MIT License (MIT)

Copyright (c) 2018 - 2019 Tilman Ginzel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```