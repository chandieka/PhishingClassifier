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
    URL_PATH = "https://storage.googleapis.com/kaggle-data-sets/55/120/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221116%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221116T111703Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=41a0f967f63675345d34c82380b8ad348195db50b47d88b7e79d830831af6fd7f167ca8d21765b41c7f7fe6c117ddaeba2ff0b6b9928c24e3ab3ea080ff655510970d3b3128d8655fc537825a1db070e58f03b860d29e272a4b65803e806843e5e839f03d38a94cb33fae035aa51806a78073b2a030db213614258bff6df623912e36b99771152da22969b82f2754d709af23d3d334f9f8e7ea825214a80c8e6d32f4c4e6b0964104ba08255f586881091cb064df9f397d38fe3956d214762600a994a5f8b111ea0ec7a5d4e04b70ee06b2899d1fb2d4b35aee97921e633c38029086e4ee757a5802a5a93e5ffd914791005640aeadbd4b8eea3b9df67d2e21d"
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