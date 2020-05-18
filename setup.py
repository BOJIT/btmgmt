import setuptools

VERSION = "v1.0.0"

with open('README.md', "r") as fh:
    long_description = fh.read()


btmgmt = setuptools.Extension('btmgmt',
                              sources=['src/btmgmt_wrapper.c',
                                       'src/bluez/src/shared/mgmt.c',
                                       'src/bluez/src/shared/util.c',
                                       'src/bluez/src/shared/queue.c',
                                       'src/bluez/src/shared/mainloop.c',
                                       'src/bluez/src/shared/io-mainloop.c',
                                       'src/bluez/src/shared/timeout-mainloop.c',
                                       'src/bluez/src/shared/mainloop-notify.c',
                                       'src/bluez/src/shared/shell.c',
                                       'src/bluez/src/shared/log.c',
                                       'src/bluez/src/uuid-helper.c'],
                              include_dirs=['src/bluez/'],
                              define_macros=[('VERSION', '\"' + VERSION + '\"')],
                              libraries=["bluetooth", "readline"]
                             )

setuptools.setup(
    name="btmgmt",
    version=VERSION,
    author="James Bennion-Pedley",
    author_email="jamesbpjames@gmail.com",
    description="simple python wrapper for the BlueZ btmgmt tool on Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BOJIT/btmgmt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    ext_modules=[btmgmt]
)
