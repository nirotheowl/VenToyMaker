#!/bin/bash

BASE_DIR="$HOME/VentoyMaker"
PY_SCRIPT="$BASE_DIR/scripts/ventoymaker.py"

if [ ! -f "$PY_SCRIPT" ]; then
  echo "Python script not found at $PY_SCRIPT"
  exit 1
fi

echo "Running VentoyMaker..."
python3 "$PY_SCRIPT"