#!/bin/sh

PYTHONPATH="$PYTHONPATH:."
export PYTHONPATH

for test in tests/*.py
do
    echo "===== $test ====="
    python3 $test
done

