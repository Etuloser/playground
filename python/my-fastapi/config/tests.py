import pytest

from config import settings


class TestConfig:
    def test_config(self):
        print(settings.db_urls)
