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

if test $# -gt 0
then
    # run tests specified on command line
    run_tests $*
else
    # run all tests
    run_tests tests/test_*.py
fi

# print report
if test -n "$failed_tests"
then
    echo "\n✘ TESTS FAILED: $failed_tests"
    exit 1
else   
    echo "\n✔ ALL TESTS PASSED"
    exit 0
fi
