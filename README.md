# flasher.py

- Tool allows firmware of esp8266, esp32 based hardware to be encapsulated in the flasher executable. Which makes easy secured firmwware distribution rather than distributing the build binary. 
- very simple command line interface, thus hidding the complex esptool options from user
- Easy to integrate with esp-idf build process

It uses [esptool.py](https://github.com/espressif/esptool) flash programming feature with a modification in `<address> <filename>` pair command line option of **write_flash** command. When `*@$` is prefixed in **filename** parameter its recognized as base64 encoded zlib compressed BLOB string, this way it allows to use in memory file IO
to upload the firmware to esp hardware in a secure way.

----------
## BLOB generator utility

**rom_blob_gen/rom_blob_gen.py** allows you to convert the firmware binary file to base64 encoded zlib compressed python string object, which cna be simply passed on through command line.

**Usage**

```shell
rom_blob_gen/rom_blob_gen.py app.bin app_rom.py
```
----------
## Generating Windows Executable

Using pyinstaller spec file we can generate single exe which includes your firmware binary and user can simply execute it. it automatically scans available serial port and uses it to upload the firmware. In case of more than one serial port was found then user can use `-p comX` to choose.

Default baud rate 921600 is defined in **flasher.py** but user can override it by using `-b <baud rate>` option. 

1. copy **flasher.py** and **flasher.spec** to some foler preferably to your esp project folder
2. **using rom_blob_gen.py** generate 3 BLOBS for bootloder as boot_rom.py, partition table as part_rom.py and application image as app_rom.py
3. make sure all 5 files [flasher.py, flasher.spec, boot_rom.py, part_rom.py, app_rom.py] in the same folder
4. Define ESP_PRJ_PATH environment variable to the folder where your are keeping the 5 files (step 3)
5. Define ESP_TOOL_PATH environment variable to folder path of your esptool installation
6. Launch command line and goto the folder (step 3), run `pyinstaller --onefile flasher.spec`
7. If everything goes well, then you should have the executable (flasher.exe) under **dist** folder


This example uploads the firmware to hardware connected in com1 @ 1.5M baud rate.
```shell
flasher.exe -p com1 -b 1500000
```