import collections
import unittest

# 具名元祖,用于构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 列表推导
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 字典初始化
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = FrenchDeck()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_random_pick_cart(self):
        # 随机抽牌
        from random import choice
        got = choice(self.deck)
        print(got)
        # Card(rank='9', suit='spades')

    def test_position(self):
        # 拿三张
        got = self.deck[:3]
        print(got)
        # 拿A,2-A共13张,从0开始,第12张为A,隔13张拿一张
        got = self.deck[12::13]
        print(got)


if __name__ == '__main__':

    # for card in sorted(deck, key=spades_high):
    #     print(card)
    unittest.main()
