from random import randint


def random_set(n, a, b):
    x_list = []
    for i in range(n):
        x = randint(a, b)
        while x in x_list:
            x = randint(a, b)
        x_list.append(x)
    return x_list


if __name__ == '__main__':
    a_len = 10
    b_len = 15
    A = random_set(a_len, 10, 100)
    B = random_set(b_len, -10, 50)
    print('A =', A)
    print('B =', B)

    import pylab

    pylab.figure(figsize=(4,3))
    pylab.grid(color='k', linestyle='-.')
    pylab.plot(range(a_len), A, 'r.')
    pylab.plot(range(b_len), B, 'k.')
    pylab.show()
