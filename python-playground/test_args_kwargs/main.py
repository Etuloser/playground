"""
https://zhuanlan.zhihu.com/p/50804195
"""


def test_args(first, *args):
    """
    output:
    Required argument:  1
    <class 'tuple'>
    Optional argument:  2
    Optional argument:  3
    Optional argument:  4
    """
    print('Required argument: ', first)
    print(type(args))  # <class 'tuple'>
    for v in args:
        print('Optional argument: ', v)


def test_kwargs(first, *args, **kwargs):
    """
    <class 'dict'>
    Optional argument (args):  2
    Optional argument (args):  3
    Optional argument (args):  4
    Optional argument k1 (kwargs): 5
    Optional argument k2 (kwargs): 6
    """
    print('Required argument: ', first)
    print(type(kwargs))
    for v in args:
        print('Optional argument (args): ', v)
    for k, v in kwargs.items():
        print('Optional argument %s (kwargs): %s' % (k, v))


if __name__ == '__main__':
    test_args(1, 2, 3, 4)
    test_kwargs(1, 2, 3, 4, k1=5, k2=6)
