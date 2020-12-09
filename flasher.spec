# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os

a = Analysis(['flasher.py'],
             pathex=[os.environ['ESP_PRJ_PATH'], os.environ['ESP_TOOL_PATH']],
             binaries=[],
             datas=[],
# add all your dependents of esptool for pyinstaller to pickup
             hiddenimports=[
                 'argparse',
                'base64',
                'binascii',
                'copy',
                'hashlib',
                'inspect',
                'io',
                'os',
                'shlex',
                'struct',
                'sys',
                'time',
                'zlib',
                'string',
                'serial.tools.list_ports',
                'serial'
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='flasher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
