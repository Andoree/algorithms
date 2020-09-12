import numpy as np


def print_subsequence_colorful(sequence, subsequence_ids):
    for i, elem in enumerate(sequence):
        if i in subsequence_ids:
            print(f"\033[93m{elem}\033[0m", end=' ')
        else:
            print(elem, end=' ')
    print()


def get_lcs_matrices(sequence_X, sequence_Y):
    m = len(sequence_X)
    n = len(sequence_Y)
    c_matrix = np.zeros(shape=(m + 1, n + 1))
    b_matrix = np.zeros(shape=(m, n), dtype=np.byte)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence_X[i - 1] == sequence_Y[j - 1]:
                c_matrix[i][j] = c_matrix[i - 1][j - 1] + 1
                b_matrix[i - 1][j - 1] = 1
            elif c_matrix[i - 1][j] >= c_matrix[i][j - 1]:
                c_matrix[i][j] = c_matrix[i - 1][j]
                b_matrix[i - 1][j - 1] = 0
            else:
                c_matrix[i][j] = c_matrix[i][j - 1]
                b_matrix[i - 1][j - 1] = -1
    return c_matrix, b_matrix


def get_lcs_and_elem_ids(c_matrix, b_matrix):
    longest_com_subseq = []
    i = b_matrix.shape[0] - 1
    j = b_matrix.shape[1] - 1
    memorized_indexes = []
    while i >= 0 and j >= 0:
        if b_matrix[i][j] == 1:
            memorized_indexes.append((i, j))
            longest_com_subseq.append(c_matrix[i + 1][j + 1])
            i -= 1
            j -= 1
        elif b_matrix[i][j] == 0:
            i -= 1
        else:
            j -= 1
    return longest_com_subseq, memorized_indexes


def main():
    X = [int(x) for x in input("Enter the first sequence:\n").split()]
    Y = [int(x) for x in input("Enter the second sequence:\n").split()]
    # X = (0, 1, 8, 13, -5, 4, 8, 9, 12, 17, 11)
    # Y = (1, 7, 4, 13, -5, 4, 9, 17, 11)
    # 0 1 8 13 -5 4 8 9 12 17 11
    # 1 7 4 13 -5 4 9 17 11
    X = np.array(X)
    Y = np.array(Y)
    c_matrix, b_matrix = get_lcs_matrices(X, Y)
    longest_com_subseq, memorized_indexes = get_lcs_and_elem_ids(c_matrix, b_matrix)

    sequence_X_elem_ids = set([t[0] for t in memorized_indexes])
    sequence_Y_elem_ids = set([t[1] for t in memorized_indexes])

    print('sequence X:', end=' ')
    print_subsequence_colorful(X, sequence_X_elem_ids)
    print('sequence Y:', end=' ')
    print_subsequence_colorful(Y, sequence_Y_elem_ids)
    print(f"Greatest common subsequence:\n{X[list(sequence_X_elem_ids)]}")


if __name__ == '__main__':
    main()
