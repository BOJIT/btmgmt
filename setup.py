import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="btmgmt",
    version="0.0.5",
    author="James Bennion-Pedley",
    author_email="jamesbpjames@gmail.com",
    description="simple python wrapper for the BlueZ btmgmt tool on Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BOJIT/btmgmt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPLv2 Licence",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
