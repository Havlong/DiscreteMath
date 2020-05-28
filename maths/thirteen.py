calculated = {0: -3 / 2, 1: 1, 2: -2}


def f(n):
    if n <= 0:
        return 0
    if n not in calculated:
        calculated[n] = -f(n - 1) + 2 * f(n - 2) + n
    return calculated[n]


def A(n):
    return int(round(n * n / 6 + 7 * n / 18 - 35 / 27 * (1 if n % 2 == 0 else -1) * (2 ** (n - 1)) - 23 / 27))


if __name__ == '__main__':
    for i in range(30, 41):
        print("a[{}] = {}, A(n) = {}".format(i, f(i), A(i)))
