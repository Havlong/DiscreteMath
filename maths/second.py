from maths.first import random_set
import pylab


def intersect(a, b):
    return [x for x in a if x in b]


def unite(a, b):
    return a + [x for x in b if x not in a]


if __name__ == '__main__':
    a_len, b_len, c_len = map(int, input().split())
    A = random_set(a_len, 0, 100)
    B = random_set(b_len, 0, 100)
    C = random_set(c_len, 0, 100)
    pylab.figure(figsize=(8, 6))
    pylab.grid(color='k', linestyle='-.')
    pylab.plot(range(a_len), A, 'ro-')
    pylab.plot(range(b_len), B, 'bo-')
    pylab.plot(range(c_len), C, 'ko-')
    pylab.show()

    short = unite(A, intersect(B, C))
    long = intersect(unite(A, B), unite(A, C))
    print('A | (B & C) =', short)
    print('(A | B) & (A | C) =', long)
    print('ok' if sorted(short) == sorted(long) else 'not ok')
