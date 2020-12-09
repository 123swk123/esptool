#!/usr/bin/env python
import sys
import zlib
import base64

if __name__ == "__main__":
    with open(sys.argv[2], 'w') as fout:
        fout.write('ROM="*@$' + base64.b64encode((zlib.compress(open(sys.argv[1], 'r+b').read(), 9))).decode('utf-8') + '"')
