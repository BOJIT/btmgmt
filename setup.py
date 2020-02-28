#!/usr/bin/env python3

from distutils.core import setup, Extension

bluez_mgmt = Extension('bluez_mgmt',
                       sources=['bluez_mgmt.c',
                                'src/shared/mgmt.c',
                                'src/shared/util.c',
                                'src/shared/queue.c',
                                'src/shared/mainloop.c',
                                'src/shared/io-mainloop.c',
                                'src/shared/timeout-mainloop.c',
                                'src/shared/mainloop-notify.c',
                                'src/shared/shell.c',
                                'src/shared/log.c',
                                'src/uuid-helper.c'],
                       include_dirs=['./'],
                       libraries=["bluetooth", "readline"])

setup(name = 'bluez_mgmt',
      version = '1.0',
      description ='A simplified Python module that uses the bluetooth \
         management API to reconfigure bluetooth adapter properties: \
         see https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/mgmt-api.txt',
      author = 'James B-P',
      ext_modules = [bluez_mgmt])
