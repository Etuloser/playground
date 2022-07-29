from configparser import ConfigParser

from influxdb import InfluxDBClient
import datetime
import time


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
                "topic": "LA08_L_NBLOG",
                "EventID": "PageLoad"
            },
            "time": datetime.datetime.utcnow(),
            # "time_precision": "s",
            "fields": {
                "ErrCode": 0,
                "Url": "http://example.com"
            }
        }
    ]
    pinflux.adds(json_body)
    result = pinflux.client.query('select * from mobile_log;')
    print("Result: {0}".format(result))
