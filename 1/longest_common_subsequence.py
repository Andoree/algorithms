import numpy as np


def main():
    # X = (0, 1, 8, 13, -5, 4)
    # Y = (1, 7, 4, 13, -5, 4)
    X = (1, 2, 3, 2, 4, 1, 2)
    Y = (2, 4, 3, 1, 2, 1)
    m = len(X)
    n = len(Y)
    c_matrix = np.zeros(shape=(m + 1, n + 1))
    b_matrix = np.zeros(shape=(m, n), dtype= np)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c_matrix[i][j] = c_matrix[i - 1][j - 1] + 1
                # todo
            elif c_matrix[i - 1][j] >= c_matrix[i][j - 1]:
                c_matrix[i][j] = c_matrix[i - 1][j]
            else:
                c_matrix[i][j] = c_matrix[i][j - 1]
                # todo
    print(c_matrix)


if __name__ == '__main__':
    main()
