#!/bin/sh

PYTHONPATH="$PYTHONPATH:."
export PYTHONPATH

python3 tests/test_cube.py
