
import math


def intsum(num=0):
    counter = 0
    while True:
        yield num
        counter += 1
        num += counter


def doubler(num=1):
    while True:
        yield num
        num *= 2


def fib(num=1):
    twoback, oneback = 0, 0
    while True:
        yield num
        twoback, oneback = oneback, num
        num = oneback + twoback


def prime(num=2):
    yield num
    num += 1
    while True:
        for x in range(3, int(math.sqrt(num)+1), 2):
            if num % x == 0:
                break
        else:
            yield num
        num += 2
