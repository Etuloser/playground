from functools import reduce
import re


def run_func(x, y):
    if x == []:
        return [y]
    for o in x:
        if str(y.values()) == str(o.values()):
            return x
        else:
            return x + [y]


if __name__ == '__main__':
    data = [{'10.252.155.161': '10.252.155'}, {'10.252.155.7': '10.252.125'},{'10.252.1asdasd': '10.252.155'}]
    for o in data:
        print(list(o.keys())[0])
