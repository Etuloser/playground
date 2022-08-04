"""
https://docs.python.org/zh-cn/3/library/threading.html
"""
import time
from threading import Thread


def func1():
    time.sleep(100)
    print('im func1')


def func2():
    time.sleep(1)
    print('im func2')


def main():
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.join()


if __name__ == '__main__':
    main()
