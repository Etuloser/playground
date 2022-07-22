"""
pip3 install tenacity
https://github.com/jd/tenacity
"""
import random
from tenacity import retry


@retry
def do_something_unreliable():
    """
    IOError will be ignore
    """
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


@retry
def never_gonna_give_you_up():
    print("Retry forever ignoring Exceptions, don't wait between retries")
    raise Exception


@retry(stop=stop_after_7_attempts(7))
def stop_after_7_attempts():
    print("Stopping after 7 attempts")
    raise Exception


if __name__ == '__main__':
    stop_after_7_attempts()