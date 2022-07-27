import time
from timeout import SetTimeout, SetTimeoutDecorator


def testSetTimeout():
    def func(a, b):
        print('[ i ] executing.')
        time.sleep(5)
        print('[ i ] execution complete, results: {}'.format(a + b))
        return a + b
    
    # test no timeout
    no_timout = SetTimeout(func, timeout=None)
    res = no_timout(a=5, b=23)
    assert res[0] and not res[1], '[ - ] timeout = None with exception res[0] / res[1]'
    assert not res[2], '[ - ] timeout = None with exception res[2]'
    assert res[3] == 28, '[ - ] timeout = None with wrong result'

    print('[ + ] no timeout ok')
    
    # test not timeout
    not_timeout = SetTimeout(func, timeout=6)
    res = not_timeout(a=5, b=23)
    assert res[0] and not res[1], '[ - ] timeout = 6 with exception res[0] / res[1]'
    assert not res[2], '[ - ] timeout = 6 with exception res[2]'
    assert res[3] == 28, '[ - ] timeout = 6 with wrong result'

    print('[ + ] not timeout ok')

    # test not timeout
    to = SetTimeout(func, timeout=3)
    res = to(a=5, b=23)
    assert not res[0] and res[1], '[ - ] timeout = 3 with exception res[0] / res[1]'
    assert not res[3], '[ - ] timeout = 3 with wrong result'

    print('[ + ] timeout ok')


def testDecorator():
    # decorator
    @SetTimeoutDecorator(timeout=3)
    def func(a, b):
        print('[ i ] executing.')
        time.sleep(5)
        print('[ i ] execution complete, results: {}'.format(a + b))
        return a + b
    res = func(a=5, b=23)
    assert not res[0] and res[1], '[ - ] decorator timeout = 3 with exception res[0] / res[1]'
    assert not res[3], '[ - ] decorator timeout = 3 with wrong result'

    print('[ + ] decorator timeout is ok')


if __name__ == '__main__':
    testSetTimeout()
    testDecorator()
