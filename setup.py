import setuptools

with open('README.md', "r") as fh:
    long_description = fh.read()


btmgmt = setuptools.Extension('btmgmt',
                              sources=['btmgmt/btmgmt.c',
                                       'btmgmt/src/shared/mgmt.c',
                                       'btmgmt/src/shared/util.c',
                                       'btmgmt/src/shared/queue.c',
                                       'btmgmt/src/shared/mainloop.c',
                                       'btmgmt/src/shared/io-mainloop.c',
                                       'btmgmt/src/shared/timeout-mainloop.c',
                                       'btmgmt/src/shared/mainloop-notify.c',
                                       'btmgmt/src/shared/shell.c',
                                       'btmgmt/src/shared/log.c',
                                       'btmgmt/src/uuid-helper.c'],
                              include_dirs=['btmgmt/'],
                              libraries=["bluetooth", "readline"]
                             )

setuptools.setup(
    name="btmgmt",
    version="0.2.0",
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
