#!/usr/bin/env python
import sys
import zlib
import base64

import boot_rom
import part_rom
import app_rom

if __name__ == "__main__":
    bytesExp = open(sys.argv[1], 'r+b').read()
    try:
        if(bytesExp == zlib.decompress(base64.b64decode(app_rom.ROM[3:].encode('utf-8')))):
            print('Matched.....')
        else:
            print('Match Failed')
    except Exception as e:
        print('Match Failed')
        print(e.__repr__())
