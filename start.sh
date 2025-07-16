#!/bin/bash

# Ensure root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (use sudo)"
  exit 1
fi

# Determine user home directory
if [ "$SUDO_USER" ]; then
  USER_HOME=$(getent passwd "$SUDO_USER" | cut -d: -f6)
else
  USER_HOME="$HOME"
fi

# Set base directory to user home
BASE_DIR="$USER_HOME/VentoyMaker"
ISO_DIR="$BASE_DIR/ISO images"
VENTOY_DIR="$BASE_DIR/ventoy"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Check Python3
if ! command -v python3 &> /dev/null; then
  echo "Python3 not found. Installing..."
  if command -v apt &> /dev/null; then
    apt update && apt install -y python3 python3-pip
  elif command -v yum &> /dev/null; then
    yum update && yum install -y python3 python3-pip
  else
    echo "Unsupported package manager. Please install Python3 and pip manually."
    exit 1
  fi
else
  echo "Python3 found."
fi

# Create necessary directories
mkdir -p "$ISO_DIR" "$VENTOY_DIR" "$BASE_DIR/scripts"

# Copy ventoymaker.py
if [ ! -f "$SCRIPT_DIR/scripts/ventoymaker.py" ]; then
  echo "Error: $SCRIPT_DIR/scripts/ventoymaker.py not found!"
  exit 1
fi

cp "$SCRIPT_DIR/scripts/ventoymaker.py" "$BASE_DIR/scripts/"
chmod +x "$BASE_DIR/scripts/ventoymaker.py"

# Final message
echo "Setup complete!"
echo "Directories created under $BASE_DIR"
echo "Put your ISO files in '$ISO_DIR'"
echo "Ventoy is downloaded in '$VENTOY_DIR'"
echo "Run your VentoyMaker script with:"
echo "  python3 $BASE_DIR/scripts/ventoymaker.py"

ln -sf "$BASE_DIR/scripts/ventoymaker.py" /usr/local/bin/ventoymaker