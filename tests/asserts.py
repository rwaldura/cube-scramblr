
pass_mark = "\033[92m✔\033[m"
fail_mark = '\033[91m✘\033[m'

def assertTrue(mesg, cond) :
    if (not cond) :
        print(fail_mark, mesg)
        assert cond
    else :
        print(pass_mark, mesg)

def assertEqual(mesg, expected, actual) :
    if (expected != actual) :
        print(fail_mark, mesg, "wanted:", expected, "got instead:", actual)
        assert False
    else :
        print(pass_mark, mesg)

def assertListEqual(mesg, expected, actual) :
    assertEqual(mesg, len(expected), len(actual))
    for i in range(len(expected)) :
        assertEqual(mesg, expected[i], actual[i])
