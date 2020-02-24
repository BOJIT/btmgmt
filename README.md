# Python Module which acts as a wrapper around the BlueZ management API:
https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/mgmt-api.txt

## Build Process:

    $ git clone https://github.com/BOJIT/bluez_mgmt

    $ sudo apt-get install $(cat dependencies.txt)

    $ cd bluez_mgmt

    $ sudo python3 setup.py build

    $ sudo python3 setup.py install

## Usage:

    import bluez_mgmt

    bluez_mgmt.command("command", "parameter1", "parameter2")
    # Variable number of arguments: arguments should be formatted as strings

## Command Index:

vailable commands:
-------------------
select <index>                                    Select a different index
version                                           Get the MGMT Version
commands                                          List supported commands
config                                            Show configuration info
info                                              Show controller info
extinfo                                           Show extended controller info
auto-power                                        Power all available features
power <on/off>                                    Toggle powered state
discov <yes/no/limited> [timeout]                 Toggle discoverable state
connectable <on/off>                              Toggle connectable state
fast-conn <on/off>                                Toggle fast connectable state
bondable <on/off>                                 Toggle bondable state
pairable <on/off>                                 Toggle bondable state
linksec <on/off>                                  Toggle link level security
ssp <on/off>                                      Toggle SSP mode
sc <on/off/only>                                  Toogle SC support
hs <on/off>                                       Toggle HS support
le <on/off>                                       Toggle LE support
advertising <on/off>                              Toggle LE advertising
bredr <on/off>                                    Toggle BR/EDR support
privacy <on/off>                                  Toggle privacy support
class <major> <minor>                             Set device major/minor class
disconnect [-t type] <remote address>             Disconnect device
con                                               List connections
find [-l|-b] [-L]                                 Discover nearby devices
find-service [-u UUID] [-r RSSI_Threshold] [-l|-b] Discover nearby service
stop-find [-l|-b]                                 Stop discovery
name <name> [shortname]                           Set local name
pair [-c cap] [-t type] <remote address>          Pair with a remote device
cancelpair [-t type] <remote address>             Cancel pairing
unpair [-t type] <remote address>                 Unpair device
keys                                              Load Link Keys
ltks                                              Load Long Term Keys
irks [--local <index>] [--file <file path>]       Load Identity Resolving Keys
block [-t type] <remote address>                  Block Device
unblock [-t type] <remote address>                Unblock Device
add-uuid <UUID> <service class hint>              Add UUID
rm-uuid <UUID>                                    Remove UUID
clr-uuids                                         Clear UUIDs
local-oob                                         Local OOB data
remote-oob [-t <addr_type>] [-r <rand192>] [-h <hash192>] [-R <rand256>] [-H <hash256>] <addr> Remote OOB data
did <source>:<vendor>:<product>:<version>         Set Device ID
static-addr <address>                             Set static address
public-addr <address>                             Set public address
ext-config <on/off>                               External configuration
debug-keys <on/off>                               Toogle debug keys
conn-info [-t type] <remote address>              Get connection information
io-cap <cap>                                      Set IO Capability
scan-params <interval> <window>                   Set Scan Parameters
get-clock [address]                               Get Clock Information
add-device [-a action] [-t type] <address>        Add Device
del-device [-t type] <address>                    Remove Device
clr-devices                                       Clear Devices
bredr-oob                                         Local OOB data (BR/EDR)
le-oob                                            Local OOB data (LE)
advinfo                                           Show advertising features
advsize [options] <instance_id>                   Show advertising size info
add-adv [options] <instance_id>                   Add advertising instance
rm-adv <instance_id>                              Remove advertising instance
clr-adv                                           Clear advertising instances
appearance <appearance>                           Set appearance
version                                           Display version
quit                                              Quit program
exit                                              Quit program
help                                              Display help about this program
export                                            Print evironment variables
