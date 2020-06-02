from math import factorial


def range_sum(n):
    return sum(map(lambda x: 1 / x, range(1, n + 1)))


def factorial_sum(n):
    return sum(
        map(lambda k: (-1 if k % 2 == 0 else 1) * factorial(n) / factorial(k) / factorial(n - k) / k, range(1, n + 1)))


if __name__ == '__main__':
    for i in [10, 25, 50]:
        print("n = {} {} == {}".format(i, range_sum(i), factorial_sum(i)))
