from configparser import ConfigParser

from influxdb import InfluxDBClient
import datetime
import time
from faker import Faker

fk = Faker()


class Pinflux:
    def __init__(self) -> None:
        self.host = ''
        self.port = ''
        self.user = ''
        self.password = ''
        self.dbname = ''
        self.client = ''

    def setup_by_configpaser(self):
        conf = ConfigParser()
        conf.read('conf.ini')
        self.host = conf.get('influxdb', 'host')
        self.port = conf.get('influxdb', 'port')
        self.user = conf.get('influxdb', 'user')
        self.password = conf.get('influxdb', 'password')
        self.dbname = conf.get('influxdb', 'dbname')

        self.client = InfluxDBClient(
            self.host,
            self.port,
            self.user,
            self.password,
            self.dbname
        )

    def create_database(self, dbname):
        self.client.create_database(dbname)

    def adds(self, json: list):
        self.client.write_points(json, database=self.dbname)

    def get(self, condition):
        return self.client.query(condition, self.dbname)


if __name__ == '__main__':
    pinflux = Pinflux()
    pinflux.setup_by_configpaser()
    json_body = [
        {
            "measurement": "mobile_log",
            "tags": {
                "domain": "www.360.com",
                "errcode": 3,
            },
            "time": time.time_ns(),
            "fields": {
                "eventid": "PageLoad"
            }
        }
    ]
    pinflux.adds(json_body)
    # result = pinflux.client.query('select * from mobile_log;')
    # docs = result.get_points()
    # for doc in docs:
    #     print(doc)
    # pinflux.client.drop_measurement('mobile_log')