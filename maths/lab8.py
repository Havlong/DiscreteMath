if __name__ == '__main__':
    n, k = map(int, input().split())
    s = [[0 for j in range(k)] for i in range(n)]
    s[0][0] = 1
    for i in range(n):
        for j in range(1, k):
            s[i][j] = s[i - 1][j - 1] + (i - 1) * s[i - 1][j]
    print('n \\ k', end='')
    for i in range(k):
        print('%7d' % i, end='')
    print()
    for i in range(n):
        print('%5d' % i, end='')
        for j in range(k):
            print('%7d' % s[i][j], end='')
        print()
