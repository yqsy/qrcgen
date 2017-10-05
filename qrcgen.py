#!/usr/bin/env python
"""
Autogenerating a qrc file from the full contents
of a directory tree
copyright 2011 by Flavio Codeco Coelho
licese: GPL v3
"""
import os
import argparse
import sys

PREFIX = None
RESNAME = None


def scan(direc):
    """
    Scan tree starting from direc
    """
    resources = []
    for path, dirs, files in os.walk(direc):
        resources += [os.path.join(path, f) for f in files]
    write_to_qrc(resources)


def write_to_qrc(resources):
    """
    Write to the qrc file under the prefix specified
    """
    with open('%s.qrc' % RESNAME.strip('/'), 'w') as f:
        f.write('<RCC>\n  <qresource prefix="%s">\n' % PREFIX)
        for r in resources:
            r = r.replace('\\', '/')
            f.write('    <file>%s</file>\n' % r)
        f.write('  </qresource>\n</RCC>\n')


def valid_path(string):
    """
    check if the path entered is a valid one
    """
    if not os.path.isdir(string):
        msg = "%s is not a valid directory" % string
        raise argparse.ArgumentTypeError(msg)
    return string


def main():
    global PREFIX
    global RESNAME
    parse = argparse.ArgumentParser(
        description='Generates a qrc (Qt resource file) from all files on a directory tree.',
        epilog='A directory.qrc file will be generated in the current directory')
    parse.add_argument('directory', metavar='directory',
                       type=valid_path,
                       help='A valid path, full or local.')
    parse.add_argument('prefix', metavar='prefix',
                       type=str,
                       help='The prefix in the qrc file under which the resources will be available.')

    # ~ parser.print_help()
    args = parse.parse_args()
    PREFIX = args.prefix
    RESNAME = os.path.split(args.directory)[-1]
    scan(args.directory)


if __name__ == "__main__":
    main()
