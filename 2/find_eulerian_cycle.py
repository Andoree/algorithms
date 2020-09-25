import numpy as np

def traverse(adjacency_matrix, start_node):
    keep_going = True
    num_vertices = len(adjacency_matrix)
    stack = []
    while keep_going:
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[start_node][j] > 0:
                stack.append(start_node)
                adjacency_matrix[start_node][j] -= 1
                start_node = j
                break
            if j == len(adjacency_matrix) - 1:
                pass
                # todo: Признать, что это тупик


def main():
    num_vertices = 5

    adjacency_matrix = np.zeros(shape=(num_vertices, num_vertices), dtype=np.int)


if __name__ == '__main__':
    main()




