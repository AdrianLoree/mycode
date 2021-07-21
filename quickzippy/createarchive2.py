#!/usr/bin/env python3

import zipfile
with open("/tmp/zipmeup/narwhal.txt", 'r') as narwhal:
    print(zipfile.is_zipfile(narwhal))
    
