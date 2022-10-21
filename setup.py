#!/usr/bin/env python3

import os
import sys


def main():
    PATHS = [
        './datasets/explored',
        './datasets/clean',
        './datasets/training',
    ]
    
    for PATH in PATHS:
        if not os.path.isdir(PATH):
            os.mkdir(PATH)

if __name__ == "__main__":
    sys.exit(main())