# btmgmt: a Python Wrapper for the BlueZ management API
see https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/mgmt-api.txt for details on how to use the API:

### tested on:
- Raspberry Pi 3B+
- Raspberry Pi 4

Built with Python 3.7, Python 2 is untested. The package can be built with bdist-wheels, but is served as a source distribution, meaning the C wrapper is compiled locally when running `pip install`. This is slightly slower, but makes the library more portable.

## Dependencies:

* *libbluetooth-dev* : the headers and source code for this extension are entirely contained
                       within this repo, but the python module is dynamically linked against
                       *lbluetooth.so* on the Linux machine.
* *libreadline-dev* : the *lreadline.so* shared library is usually installed by default, but
                      C header files are required to build this module from source.

## Install Process:

    $ sudo apt-get install libbluetooth-dev libreadline-dev

    $ sudo pip3 install btmgmt

    # most of the BTMGMT commands require root privileges, so the library should be
    # installed to the root python environment.

## Usage:

    # Demonstrative only: see example scripts for more information

    import btmgmt

    btmgmt.command("command", "parameter1", "parameter2")

    # Variable number of arguments allowed depending on the command (see below).

## Permissions:

If you do not want to run as root, simply set the capabilities of the process (in this case, Python) to have `CAP_NET_ADMIN`.

    sudo setcap cap_net_admin+eip $(readlink -f $(which python3))

You can verify that this is `OK` by running the above command with verify flag:

    sudo setcap -v cap_net_admin+eip $(readlink -f $(which python3))

## Available Commands:

> `select <index>                                    Select a different index`<br>
> `version                                           Get the MGMT Version`<br>
> `commands                                          List supported commands`<br>
> `config                                            Show configuration info`<br>
> `info                                              Show controller info`<br>
> `extinfo                                           Show extended controller info`<br>
> `auto-power                                        Power all available features`<br>
> `power <on/off>                                    Toggle powered state`<br>
> `discov <yes/no/limited> [timeout]                 Toggle discoverable state`<br>
> `connectable <on/off>                              Toggle connectable state`<br>
> `fast-conn <on/off>                                Toggle fast connectable state`<br>
> `bondable <on/off>                                 Toggle bondable state`<br>
> `linksec <on/off>                                  Toggle link level security`<br>
> `ssp <on/off>                                      Toggle SSP mode`<br>
> `sc <on/off/only>                                  Toogle SC support`<br>
> `hs <on/off>                                       Toggle HS support`<br>
> `le <on/off>                                       Toggle LE support`<br>
> `advertising <on/off>                              Toggle LE advertising`<br>
> `bredr <on/off>                                    Toggle BR/EDR support`<br>
> `privacy <on/off>                                  Toggle privacy support`<br>
> `class <major> <minor>                             Set device major/minor class`<br>
> `disconnect [-t type] <remote address>             Disconnect device`<br>
> `con                                               List connections`<br>
> `find [-l|-b] [-L]                                 Discover nearby devices`<br>
> `find-service [-u UUID] [-r RSSI_Threshold] [-l|-b] Discover nearby service`<br>
> `stop-find [-l|-b]                                 Stop discovery`<br>
> `name <name> [shortname]                           Set local name`<br>
> `pair [-c cap] [-t type] <remote address>          Pair with a remote device`<br>
> `cancelpair [-t type] <remote address>             Cancel pairing`<br>
> `unpair [-t type] <remote address>                 Unpair device`<br>
> `keys                                              Load Link Keys`<br>
> `ltks                                              Load Long Term Keys`<br>
> `irks [--local <index>] [--file <file path>]       Load Identity Resolving Keys`<br>
> `block [-t type] <remote address>                  Block Device`<br>
> `unblock [-t type] <remote address>                Unblock Device`<br>
> `add-uuid <UUID> <service class hint>              Add UUID`<br>
> `rm-uuid <UUID>                                    Remove UUID`<br>
> `clr-uuids                                         Clear UUIDs`<br>
> `local-oob                                         Local OOB data`<br>
> `remote-oob [-t <addr_type>] [-r <rand192>] [-h <hash192>] [-R <rand256>] [-H <hash256>] <addr> Remote OOB data`<br>
> `did <source>:<vendor>:<product>:<version>         Set Device ID`<br>
> `static-addr <address>                             Set static address`<br>
> `public-addr <address>                             Set public address`<br>
> `ext-config <on/off>                               External configuration`<br>
> `debug-keys <on/off>                               Toogle debug keys`<br>
> `conn-info [-t type] <remote address>              Get connection information`<br>
> `io-cap <cap>                                      Set IO Capability`<br>
> `scan-params <interval> <window>                   Set Scan Parameters`<br>
> `get-clock [address]                               Get Clock Information`<br>
> `add-device [-a action] [-t type] <address>        Add Device`<br>
> `del-device [-t type] <address>                    Remove Device`<br>
> `clr-devices                                       Clear Devices`<br>
> `bredr-oob                                         Local OOB data (BR/EDR)`<br>
> `le-oob                                            Local OOB data (LE)`<br>
> `advinfo                                           Show advertising features`<br>
> `advsize [options] <instance_id>                   Show advertising size info`<br>
> `add-adv [options] <instance_id>                   Add advertising instance`<br>
> `rm-adv <instance_id>                              Remove advertising instance`<br>
> `clr-adv                                           Clear advertising instances`<br>
> `appearance <appearance>                           Set appearance`<br>
> `version                                           Display version`<br>
> `quit                                              Quit program`<br>
> `exit                                              Quit program`<br>
> `help                                              Display help about this program`<br>
> `export                                            Print evironment variables`<br>
