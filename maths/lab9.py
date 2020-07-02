from scipy.special import comb


def combinations(n, k):
    return comb(n, k, exact=True)  # При n < 0 результат 0


if __name__ == '__main__':
    n, k = map(int, input().split())
    c = combinations(n, k)
    s = sum(map(lambda r: combinations(n - r - 1, k - r), range(n + 1)))
    print('Equal' if c == s else 'Not equal')
