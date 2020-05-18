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

adapter_name_long = input("Enter Long Adapter Name:")
adapter_name_short = input("Enter Short Adapter Name:")

if bluez_mgmt.command("name", adapter_name_long, adapter_name_short) != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("info") != 0:
    sys.exit(RETURN_ERROR)

# Adapter must be turned off to change LE or BR/EDR modes.
if bluez_mgmt.command("power", "off") != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("bredr", "on") != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("le", "off") != 0:
    sys.exit(RETURN_ERROR)

if bluez_mgmt.command("power", "on") != 0:
    sys.exit(RETURN_ERROR)

# Get new configuration to check our changes were successful.

print("Final Configuration:")

bluez_mgmt.command("info")

sys.exit(RETURN_DEFAULT)
