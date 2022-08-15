import unittest
# abstract base classes 抽象基类
from collections import abc


class TestDict(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_dict_type(self):
        my_dict = {}
        # dict是抽象基类Mapping的实现,是一个泛映射类型
        got = isinstance(my_dict, abc.Mapping)
        print(got)  # True

    def test_dict_method(self):
        my_dict = {}
        # 可散列对象必须实现__hash__(),__eq__()方法,只需键可散列,值不用
        has_hash = hasattr(my_dict, '__hash__')
        has_eq = hasattr(my_dict, '__eq__')
        print(has_hash, has_eq)

    def test_built_in_dict(self):
        # dict关键字构造
        a = dict(one=1, two=2, three=3)
        # 直接声明
        b = {'one': 1, 'two': 2, 'three': 3}
        # 元祖压缩
        c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
        d = dict([('two', 2), ('one', 1), ('three', 3)])
        e = dict({'three': 3, 'one': 1, 'two': 2})
        print(a == b == c == d == e)


if __name__ == '__main__':
    unittest.main()
