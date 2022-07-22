"""
https://docs.python.org/3/library/functions.html
内置函数
"""
import unittest


class TestBuiltInFunction(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_filter(self):
        strs = ['a', 'ab', 'abc', 'python']
        y = filter(lambda s: len(s) > 2, strs)
        tmp = list(map(lambda s: s.upper(), y))
        print(tmp)
