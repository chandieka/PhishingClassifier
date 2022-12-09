#!/usr/bin/env python3

import os
import sys
import urllib.request
from zipfile import ZipFile 


def main():
    PATHS = [
        './datasets/explored',
        './datasets/clean',
        './datasets/training',
        './datasets/test'
    ]
    
    print("[1] Creating Directories")
    for PATH in PATHS:
        if not os.path.isdir(PATH):
            os.mkdir(PATH)
            
    print("[2] Downloading datasets from kaggle")
    URL_PATH = "https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/download?datasetVersionNumber=2"
    with urllib.request.urlopen(URL_PATH) as f:
        archive = f.readlines()
        with open('./datasets/raw/archive.zip', 'wb') as zip:
            zip.writelines(archive)
            
    print("[3] Extracting datasets")
    with ZipFile('./datasets/raw/archive.zip', mode='r') as zp:
        zp.extractall('./datasets/raw/')
    
    print('[4] Cleaning up')
    os.remove('./datasets/raw/archive.zip')

if __name__ == "__main__":
    sys.exit(main())