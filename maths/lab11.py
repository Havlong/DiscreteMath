from maths.lab1 import random_set
from maths.lab2 import intersect


def get_all_subsets(full_set):
    core = range(len(full_set))
    max_mask = 1 << len(full_set)
    mask = 0
    all_subsets = []
    while mask < max_mask:
        subset = []
        for bit in core:
            if (mask >> bit) & 1:
                subset.append(full_set[bit])
        mask += 1
        all_subsets.append(subset)

    return sorted(all_subsets, key=lambda x: len(x))


if __name__ == '__main__':
    print('Please enter universum size')
    n = int(input())
    universum = sorted(random_set(n, -40, 40))
    print('Universum is:', universum)
    subsets = get_all_subsets(universum)
    print('Number of subsets is:', len(subsets))
    print('Subsets:', subsets)
    count = 0
    for i in range(len(subsets)):
        for j in range(i + 1, len(subsets)):
            if len(intersect(subsets[i], subsets[j])) == 0:
                count += 1
    print(count)
