def full_a(n, k):
    return n ** k


def partial_a(n, k):
    answer = 1
    for i in range(n - k + 1, n + 1):
        answer *= i
    return answer


if __name__ == '__main__':
    m, k = map(int, input().split())
    variants = len([0, 1])
    print('a)', full_a(full_a(variants, k), m))
    print('b)', partial_a(full_a(variants, k), m))
