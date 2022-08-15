"""
https://docs.python.org/3/library/functions.html
内置函数
"""
import unittest
import functools


class TestBuiltInFunction(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_filter(self):
        strs = ['a', 'ab', 'abc', 'python']
        # filter(function, iterable) 当 function 不是 None 的时候为 (item for item in iterable if function(item))；function 是 None 的时候为 (item for item in iterable if item) 。
        y = filter(lambda s: len(s) > 2, strs)
        # map(function, iterable, ...)
        tmp = list(map(lambda s: s.upper(), y))
        print(tmp)

    def test_reduce(self):
        # remove duplicate element in dict list
        dict_list = [{'a': 1}, {'b': 1}, {'c': 1}, {'a': 1}]
        got = functools.reduce(
            lambda x, y: x if y in x else x + [y], [[], ]+dict_list)
        print(got)


if __name__ == '__main__':
    unittest.main()
