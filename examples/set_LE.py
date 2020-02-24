# Example usage of bluez_mgmt Python Wrapper:
# Scripts must be run as Root!

import sys
import bluez_mgmt

RETURN_ERROR = -1
RETURN_DEFAULT = 0


# Return from command is printed to stdout by default.
# To parse returned information, the output must be redirected.

print("Initial Configuration:")

bluez_mgmt.command("info")

adapter_name = input("Enter Adapter Name:")

if bluez_mgmt.command("name", adapter_name) != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("info") != 0:
    sys.exit(RETURN_ERROR)

# Adapter must be turned off to change LE or BR/EDR modes.
if bluez_mgmt.command("power", "off") != 0:
    sys.exit(RETURN_ERROR)

# Most bluetooth adapters will return an error if you disable both LE and BR/EDR
# modes simultaneously, so if unsure of the initial state of the peripheral,
# enable both modes (Dual Mode) before disabling one.

if bluez_mgmt.command("bredr", "on") != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("le", "on") != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("bredr", "off") != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("power", "on") != 0:
    sys.exit(RETURN_ERROR)

# Get new configuration to check our changes were successful.

print("Final Configuration:")

bluez_mgmt.command("info")

sys.exit(RETURN_DEFAULT)
