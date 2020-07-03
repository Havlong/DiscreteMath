from random import randint


def random_set_triplets(n, a, b):
    # n - кол-во элементов, а и b - границы выбора случайных элементов
    # Возвращает список триплетов вида (элемент, вес, ценность)
    x_list = []
    for i in range(n):
        x = randint(a, b)
        while x in x_list:
            x = randint(a, b)
        x_list.append(x)
    return [(i, randint(1, 10), randint(1, 10)) for i in x_list]


def next_grey(x, t):
    # x - предыдущий код Грея, t - номер кода
    # Возвращает следующий код Грея
    return x ^ (t - (t & (t - 1)))  # Оставляем от номера кода только последнюю 1 в двоичной записи и проводим xor


def count_bits(x):
    # x - число
    # Возвращает число 1 в двоичной записи
    count = 0
    while x > 0:
        count += 1
        x &= x - 1  # Отрезаем последнюю 1
    return count


def k_subsets(A, k):
    # А - множество, k - количество элементов для выбора из множества
    # Возвращает триплет (код Грея, вес, ценность) лучшего подмножестве
    code = 0
    n = len(A)
    min_w = 10 * k
    max_v = 0
    best = 0
    for t in range(1, 2 ** n):
        code = next_grey(code, t)  # Получаем следующий код
        if count_bits(code) == k:  # Если 1 столько, сколько должно быть элементов в подмножестве
            w = 0
            v = 0
            for i in range(n):
                if code & (1 << i) > 0:  # Если на i-ой позиции в коде есть 1
                    w += A[i][1]  # Сумма весов
                    v += A[i][2]  # Сумма ценностей
            if w < min_w or (w == min_w and v > max_v):  # Когда результат улучшен
                best = code
                min_w = w
                max_v = v
    return best, min_w, max_v


if __name__ == '__main__':
    A = random_set_triplets(5, -10, 10)  # Получаем множество
    print('Set A:')
    print(*A)
    result, weight, value = k_subsets(A, 3)
    print('Answer from code {0:b} with weight {1} and value {2} is:'.format(result, weight, value))
    answer = []  # Восстанавливаем подмножество
    for i in range(len(A)):
        if result & (1 << i) > 0:  # Если на i-ой позиции в коде есть 1
            answer.append(A[i][0])
    print(*answer)
