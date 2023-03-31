import pytest

from config import settings
from pkg.mysql import Client
from sqlalchemy import text


class TestMysql:
    client = Client()
    engine = client.new_engine(settings.db_url)

    def test_new_engine(self):
        engine = self.client.new_engine(settings.db_url)
        assert engine is not None

    def test_exec_raw_sql(self):
        queryset = self.engine.connect().execute(text("SHOW VARIABLES"))
        for obj in queryset:
            print(obj)
