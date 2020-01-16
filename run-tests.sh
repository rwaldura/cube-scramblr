#!/bin/sh

PYTHONPATH="$PYTHONPATH:.:src"
export PYTHONPATH

failed_tests=""

run_tests()
    for test in $*
    do
        echo "\n•••••• $test ••••••"
        if python3 $test
        then    
            : # test passed
        else
            # test failed, keep track of it
            failed_tests="$failed_tests $test"
        fi
    done

if [ $# -eq 0 ]
then
    # run all tests
    run_tests tests/test_*.py
else
    # run tests specified on command line
    run_tests $*
fi

# print report
if test -n "$failed_tests"
then
    # bright bold red
    echo "\n\033[91;1m✘ TESTS FAILED: \033[0m$failed_tests"
    exit 1
else   
    # bright bold green
    echo "\n\033[92;1m✔ ALL TESTS PASSED\033[0m"
    exit 0
fi
