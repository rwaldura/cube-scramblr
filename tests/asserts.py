
pass_mark = '✔'
fail_mark = '✘'

def assertTrue(mesg, cond) :
    if (not cond) :
        print(fail_mark, mesg)
        assert cond
    else :
        print(pass_mark, mesg)

def assertEqual(mesg, expected, actual) :
    if (expected != actual) :
        print(fail_mark, mesg, "expected", expected, "but got instead", actual)
        assert False
    else :
        print(pass_mark, mesg)

def assertListEqual(mesg, expected, actual) :
    assertEqual(mesg, len(expected), len(actual))
    for i in range(len(expected)) :
        assertEqual(mesg, expected[i], actual[i])
