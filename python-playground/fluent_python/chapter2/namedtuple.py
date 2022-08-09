"""
https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple
"""
from collections import namedtuple

# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
# field_names 可以是一个字符串序列，或者用空格/逗号隔开的字符串
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

if __name__ == '__main__':
    from ..chapter1.french_deck import FrenchDeck
    