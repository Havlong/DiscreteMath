def list_to_matrix(a, b, p):
    return [[1 if (a[i], b[j]) in p else 0 for j in range(len(b))] for i in range(len(a))]


def intersect_matrices(matrix_a, matrix_b):
    return [[min(matrix_a[i][j], matrix_b[i][j]) for j in range(len(matrix_a[i]))] for i in range(len(matrix_a))]


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]


def hadamard_product(matrix_a, matrix_b):
    return [[matrix_a[i][j] * matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]


if __name__ == '__main__':
    A = [0, 1, 2, 3, 4]
    B = ['z', 'y', 'x', 'w', 'v']
    delta = [(0, 'v'), (1, 'y'), (2, 'w'), (3, 'z'), (4, 'x')]
    ro = [(0, 'z'), (1, 'y'), (2, 'x'), (3, 'w'), (4, 'v')]
    delta_matrix = list_to_matrix(A, B, delta)
    ro_matrix = list_to_matrix(A, B, ro)
    intersect_matrix = intersect_matrices(delta_matrix, ro_matrix)

    print('delta is')
    print(*delta_matrix, sep='\n')
    print('ro is')
    print(*ro_matrix, sep='\n')
    print('Intersection is')
    print(*intersect_matrix, sep='\n')
    delta = [('v', 0), ('y', 1), ('w', 2), ('z', 3), ('x', 4)]
    intersection = intersect_matrices(delta_matrix, list_to_matrix(B, A, delta))
    multiplication = hadamard_product(delta_matrix, transpose_matrix(delta_matrix))
    print('Rule check is', 'positive' if (intersection == multiplication) else 'negative')
