import sys

try:
    import part_rom
    import boot_rom
    import app_rom
except Exception as e:
    print('Error: ROM files are missing...')
    #print(e.__repr__())
    sys.exit(-1)

try:
    import esptool
except KeyError:
    print('Error: unable to find esptool')
    sys.exit(-1)

bFoundBaud = False
for arg in sys.argv:
    if arg == '-b' or arg == '--baud':
        bFoundBaud = True
        break

if bFoundBaud == False:
    sys.argv = sys.argv + ['-b', '921600']

sys.argv = sys.argv + ['write_flash', '--flash_mode', 'dio', '--flash_freq', '80m', '--flash_size', '2MB']
sys.argv = sys.argv + ['0x8000', part_rom.ROM]
sys.argv = sys.argv + ['0x0', boot_rom.ROM]
sys.argv = sys.argv + ['0x10000', app_rom.ROM]

if __name__ == "__main__":
    try:
        esptool.main()
    except esptool.FatalError as identifier:
        pass
