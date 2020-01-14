#!/bin/sh

PYTHONPATH="$PYTHONPATH:..:../src"
export PYTHONPATH

cd tests

for test in test_*.py
do
    echo "\n•••••• $test ••••••"
    python3 $test
done

