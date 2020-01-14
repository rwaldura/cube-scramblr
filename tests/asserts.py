def assertTrue(mesg, cond) :
    if (not cond) :
        print("FAIL:", mesg)
        assert cond
    else :
        print("pass:", mesg)

def assertEqual(mesg, expected, actual) :
    if (expected != actual) :
        print("FAIL:", mesg, "expected", expected, "but got instead", actual)
        assert False
    else :
        print("pass:", mesg)

def assertListEqual(mesg, expected, actual) :
    assertEqual(mesg, len(expected), len(actual))
    for i in range(len(expected)) :
        assertEqual(mesg, expected[i], actual[i])
