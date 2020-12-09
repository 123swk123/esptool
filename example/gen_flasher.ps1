python ..\rom_blob_gen\rom_blob_gen.py .\build\gpio.bin app_rom.py
python ..\rom_blob_gen\rom_blob_gen.py .\build\bootloader\bootloader.bin boot_rom.py
python ..\rom_blob_gen\rom_blob_gen.py .\build\partition_table\partition-table.bin part_rom.py

$env:ESP_TOOL_PATH='C:\Users\self\esptool_flasher'
$env:ESP_PRJ_PATH='C:\Users\self\esptool_flasher\example'
pyinstaller --onefile flasher.spec