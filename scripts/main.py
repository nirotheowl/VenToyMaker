#!/usr/bin/env python3
import os
import sys
import subprocess
import urllib.request
import shutil
import pwd

# Get the absolute directory this script lives in
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ISO_DIR = os.path.join(BASE_DIR, 'ISO images')
SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')
VENTOY_DIR = os.path.join(BASE_DIR, 'ventoy')
VENTOY_VERSION = '1.1.05'
VENTOY_TAR = f'ventoy-{VENTOY_VERSION}-linux.tar.gz'
VENTOY_URL = f'https://github.com/ventoy/Ventoy/releases/download/v{VENTOY_VERSION}/{VENTOY_TAR}'
MOUNT_POINT = '/mnt/ventoy_usb'

# Ensure the wizard script is importable
sys.path.insert(0, SCRIPTS_DIR)
from wizard import run_wizard

def prompt_yes_no(question):
    while True:
        ans = input(question + ' (y/n): ').lower()
        if ans in ['y', 'yes']:
            return True
        elif ans in ['n', 'no']:
            return False

def create_dirs():
    missing = []
    for d in [ISO_DIR, SCRIPTS_DIR, VENTOY_DIR]:
        if not os.path.isdir(d):
            missing.append(d)
    if missing:
        print('Missing directories detected:')
        for d in missing:
            print('  ' + d)
        if prompt_yes_no('Create missing directories?'):
            for d in missing:
                os.makedirs(d)
                print(f'Created: {d}')
        else:
            print('Aborted.')
            sys.exit(1)

def detect_usb_devices():
    print('Detecting removable USB drives...')
    try:
        result = subprocess.run(['lsblk', '-o', 'NAME,RM,SIZE,MODEL'], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')[1:]
        devices = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 4 and parts[1] == '1':
                devices.append({
                    'name': parts[0],
                    'size': parts[2],
                    'model': ' '.join(parts[3:])
                })
        if not devices:
            print('No removable USB devices detected. Please plug in your USB drive and rerun.')
            sys.exit(1)
        print('Available USB devices:')
        for i, dev in enumerate(devices):
            print(f'  [{i}] /dev/{dev["name"]} - {dev["model"]} - {dev["size"]}')
        while True:
            choice = input('Select device number to use: ')
            if choice.isdigit() and 0 <= int(choice) < len(devices):
                return '/dev/' + devices[int(choice)]['name']
            print('Invalid choice, try again.')
    except Exception as e:
        print(f'Error detecting USB devices: {e}')
        sys.exit(1)

def download_ventoy():
    ventoy_path = os.path.join(VENTOY_DIR, VENTOY_TAR)
    if not os.path.isfile(ventoy_path):
        print(f'Downloading Ventoy {VENTOY_VERSION}...')
        urllib.request.urlretrieve(VENTOY_URL, ventoy_path)
        print('Download complete.')
        print('Extracting Ventoy...')
        shutil.unpack_archive(ventoy_path, VENTOY_DIR)
        print('Extraction complete.')
    else:
        print('Ventoy archive already exists.')

def install_ventoy(usb_device):
    ventoy_folder = os.path.join(VENTOY_DIR, f'ventoy-{VENTOY_VERSION}')
    installer_path = os.path.join(ventoy_folder, 'Ventoy2Disk.sh')
    if not os.path.isfile(installer_path):
        print(f'Ventoy installer not found at {installer_path}')
        sys.exit(1)
    print(f'Installing Ventoy on {usb_device} (this will erase all data)...')
    try:
        subprocess.run(['sudo', installer_path, '-i', usb_device], check=True)
        print('Ventoy installation completed.')
    except subprocess.CalledProcessError:
        print('Ventoy installation failed.')
        sys.exit(1)

def mount_usb(usb_device):
    part1 = usb_device + '1'
    if not os.path.exists(MOUNT_POINT):
        os.makedirs(MOUNT_POINT)
    subprocess.run(['sudo', 'umount', MOUNT_POINT], stderr=subprocess.DEVNULL)
    print(f'Mounting {part1} to {MOUNT_POINT} with user ownership...')
    uid = str(os.getuid())
    gid = str(os.getgid())
    try:
        subprocess.run(['sudo', 'mount', '-o', f'uid={uid},gid={gid}', part1, MOUNT_POINT], check=True)
        print('Mounted.')
    except subprocess.CalledProcessError:
        print('Failed to mount Ventoy USB partition.')
        sys.exit(1)

def copy_isos():
    if not os.path.isdir(ISO_DIR):
        print(f'ISO folder {ISO_DIR} does not exist.')
        sys.exit(1)
    files = [f for f in os.listdir(ISO_DIR) if f.lower().endswith('.iso')]
    if not files:
        print(f'No ISO files found in {ISO_DIR}.')
        return
    print(f'Copying {len(files)} ISO files to Ventoy USB...')
    for f in files:
        src = os.path.join(ISO_DIR, f)
        dst = os.path.join(MOUNT_POINT, f)
        shutil.copy2(src, dst)
        print(f'Copied: {f}')
    print('All ISOs copied.')

def main():
    create_dirs()
    run_wizard(ISO_DIR)
    input(f'Please place your ISO files into:\n  {ISO_DIR}\nPress Enter to continue...')
    usb_device = detect_usb_devices()
    if not prompt_yes_no(f'WARNING: This will erase all data on {usb_device}. Proceed?'):
        print('Aborted.')
        sys.exit(0)
    download_ventoy()
    install_ventoy(usb_device)
    mount_usb(usb_device)
    copy_isos()
    subprocess.run(['sudo', 'umount', MOUNT_POINT])
    print('Done! You can now boot from your Ventoy USB.')

if __name__ == '__main__':
    main()
