# coding=utf-8
import logging
import time

logging.warning("Watch out!")  # WARNING:root:Watch out!

# default logging level is waring
# so info level log will not print
# log level: DEBUG->INFO->WARNING->ERROR->CRITICAL
logging.info('I told you so')

logging.basicConfig(filename='example.log', filemode='w',
                    encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def main():
    logging.basicConfig(filename='example.log', level=logging.INFO)
    logging.info('Started')
    time.sleep(1)
    logging.info('Finished')


if __name__ == '__main__':
    main()
