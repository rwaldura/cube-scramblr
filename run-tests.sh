#!/bin/sh

PYTHONPATH="$PYTHONPATH:.:src"
export PYTHONPATH

run_tests()
    for test in $*
    do
        echo "\n•••••• $test ••••••"
        python3 $test
    done

if test $# -gt 0
then
    # run tests specified on command line
    run_tests $*
else
    # run all tests
    run_tests tests/test_*.py
fi
