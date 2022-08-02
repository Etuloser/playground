"""
python -m unittest main.TestFaker.test_fake_name
"""
import unittest

from faker import Faker


class TestFaker(unittest.TestCase):
    def setUp(self) -> None:
        self.fake = Faker()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_fake_name(self):
        for _ in range(10):
            print(self.fake.name())
