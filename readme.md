
<!-- TOC -->

- [1. help](#1-help)
- [2. pip install](#2-pip-install)

<!-- /TOC -->

# 1. help
This Script generates a qrc file (Qt Resource file) for the entire contents of a directory tree.


usage: qrcgen.py [-h] directory prefix

Generates a qrc (Qt resource file) from all files on a directory tree.

positional arguments:
  directory   A valid path, full or local.
  prefix      The prefix in the qrc file under which the resources will be
              available.

optional arguments:
  -h, --help  show this help message and exit

A directory.qrc file will be generated in the current directory


# 2. pip install

```
pip install git+https://github.com/yqsy/qrcgen
```