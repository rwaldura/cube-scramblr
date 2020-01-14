#!/bin/sh

PYTHONPATH="$PYTHONPATH:.:src"
export PYTHONPATH

for test in tests/test_*.py
do
    echo "===== $test ====="
    python3 $test
done

