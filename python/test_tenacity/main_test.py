import unittest
from test_tenacity.main import do_something_unreliable


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_do_something_unreliable(self):
        got = do_something_unreliable()
        print(got)
