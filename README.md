██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██╗   ██╗
██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗╚██╗ ██╔╝
██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║ ╚████╔╝ 
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║  ╚██╔╝  
 ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝    ╚═╝   
                                                      
  ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗            
  ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗           
  ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝           
  ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗           
  ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║           
  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝           
                                                  


VentoyMaker is a simple Python-based utility to help create a bootable Ventoy USB drive and copy existing `.iso` files onto it. It is designed for users who want to quickly set up a multiboot USB stick with minimal effort.

## Features

- Automatically downloads and extracts Ventoy for Linux
- Detects and lists removable USB drives
- Installs Ventoy with user confirmation
- Mounts the USB drive with correct user permissions
- Copies `.iso` files from a local folder to the USB
- Optional interactive wizard to help find `.iso` files

## Directory Layout

VentoyMaker/
├── scripts/
│   ├── main.py          (Main program you run)
│   └── wizard.py        (Optional helper for locating ISO files)
├── ISO images/          (Where you place your .iso files)
├── ventoy/              (Ventoy download and extraction target)

## Usage

1. Extract the VentoyMaker files to a working directory.
2. Run the script using:

   sudo python3 scripts/main.py

   The script requires `sudo` to mount USB devices and run the Ventoy installer.

3. Follow the prompts:
   - Optionally launch the ISO wizard
   - Choose the USB device to use
   - Confirm installation (this will erase the selected USB drive)
   - ISO files in the `ISO images/` folder will be copied automatically

## Warning

This script will erase the selected USB drive during installation. Make sure you select the correct device (such as /dev/sdb) and back up any important data beforehand.

## Requirements

- Python 3.6 or higher
- Linux operating system
- Must have the following tools available:
  - `lsblk`, `mount`, `umount`
  - Internet access for downloading Ventoy

## ISO Files

You can place `.iso` files into the `ISO images/` folder manually, or let the optional wizard assist you in locating existing `.iso` files on your system. These will be copied to the USB drive after Ventoy is installed and mounted.

## Troubleshooting

- If no USB drives are detected, check that your USB drive is inserted and readable.
- If installation fails, ensure you have `sudo` privileges and the USB is not mounted elsewhere.
- If ISO files aren't copied, check that they exist in the `ISO images/` folder and that the USB partition is mounted properly.

## License

VentoyMaker is released under the MIT License. Ventoy itself is developed independently and is available at:

https://github.com/ventoy/Ventoy
