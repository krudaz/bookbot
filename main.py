#!/usr/bin/python3

import sys


def main(filename):

    with open(filename, 'r') as file:
        print(file.read())


if __name__ == "__main__":
    main(sys.argv[1])

