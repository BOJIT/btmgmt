# Python Module which acts as a wrapper around the BlueZ management API:
https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/mgmt-api.txt

## Build Process:

    $ git clone https://github.com/BOJIT/bluez_mgmt

    $ sudo apt-get install $(cat dependencies.txt)

    $ cd bluez_mgmt

    $ sudo python3 setup.py build

    $ sudo python3 setup.py install
