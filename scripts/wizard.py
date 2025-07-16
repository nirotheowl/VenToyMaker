#!/usr/bin/env python3

import os
import shutil

COMMON_ISO_NAMES = [
    "ubuntu", "kali", "mint", "debian", "windows10", "windows11",
    "fedora", "arch", "manjaro"
]

SEARCH_DIRS = [
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Desktop"),
    "/iso", "/isos"
]

def scan_for_isos():
    found = []
    print("Scanning for ISO files...")
    if not any(os.path.isdir(d) for d in SEARCH_DIRS):
        print("No known ISO directories found. You may need to add ISOs manually.")
        return found

    for directory in SEARCH_DIRS:
        if os.path.isdir(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(".iso"):
                        full_path = os.path.join(root, file)
                        found.append(full_path)
    return found

def suggest_common_isos():
    print("\nCommon ISOs you may want to download manually:")
    for iso in COMMON_ISO_NAMES:
        print(f"  - {iso.title()} ISO")

def move_selected_isos(found_isos, iso_dir):
    if not found_isos:
        print("No ISOs found automatically.")
        suggest_common_isos()
        return

    print("\nFound ISO files:")
    for idx, iso in enumerate(found_isos):
        print(f"[{idx}] {iso}")

    choices = input("\nEnter the numbers of the ISOs to move (comma-separated), or 'n' to skip: ").strip().lower()
    if choices == 'n':
        return

    indices = []
    for i in choices.split(','):
        i = i.strip()
        if i.isdigit():
            idx = int(i)
            if 0 <= idx < len(found_isos):
                indices.append(idx)
            else:
                print(f"Index {idx} out of range. Skipping.")

    os.makedirs(iso_dir, exist_ok=True)

    for i in indices:
        try:
            src = found_isos[i]
            dst = os.path.join(iso_dir, os.path.basename(src))
            shutil.copy2(src, dst)
            print(f"Copied: {src} -> {dst}")
        except Exception as e:
            print(f"Failed to copy {found_isos[i]}: {e}")

def run_wizard(iso_dir):
    print("\n--- VentoyMaker Setup Wizard ---")
    if input("Would you like to run the wizard? (y/n): ").strip().lower() != 'y':
        return

    if input("Scan for existing ISO files on your system? (y/n): ").strip().lower() == 'y':
        found = scan_for_isos()
        move_selected_isos(found, iso_dir)
    else:
        suggest_common_isos()

    print(f"\nYou can add more ISOs manually to: {iso_dir}")
