import numpy as np


def traverse_nodes(adjacency_matrix, start_node, tmp_stack):
    keep_going = True
    new_start_node = start_node
    cycle_exists = True
    while keep_going:
        for j in range(len(adjacency_matrix)):
            if j != len(adjacency_matrix) - 1 and adjacency_matrix[new_start_node][j] > 0:
                tmp_stack.append(new_start_node)
                adjacency_matrix[new_start_node][j] -= 1
                new_start_node = j
                break
            elif j == len(adjacency_matrix) - 1:
                if adjacency_matrix[new_start_node][j] > 0:
                    tmp_stack.append(new_start_node)
                    adjacency_matrix[new_start_node][j] -= 1
                    new_start_node = j
                else:
                    keep_going = False
    if start_node != new_start_node:
        cycle_exists = False
    return cycle_exists


def find_eulerian_cycle(adjacency_matrix):
    tmp_stack = [0, ]
    final_stack = []
    path_exists = True
    while path_exists and len(tmp_stack) > 0:
        start_node = tmp_stack.pop()
        final_stack.append(start_node)
        path_exists = traverse_nodes(adjacency_matrix, start_node, tmp_stack)
    if path_exists:
        return final_stack
    else:
        return [-1, ]


def main():
    nodes = []
    with open("input.txt", 'r', encoding="utf-8") as inp_file:
        num_vertices = int(inp_file.readline().strip())
        line = inp_file.readline()
        while line != "":
            attrs = [int(x) for x in line.strip().split(",")]
            nodes.append((attrs[0], attrs[1]))
            line = inp_file.readline()

    adjacency_matrix = np.zeros(shape=(num_vertices, num_vertices), dtype=np.int)
    for (from_node, to_node) in nodes:
        adjacency_matrix[from_node][to_node] += 1
    print("Матрица смежности:\n", adjacency_matrix, end='')
    eulirean_cycle = find_eulerian_cycle(adjacency_matrix)
    if eulirean_cycle[0] == -1:
        print("Eulerian path does not exist")
    else:
        eulirean_cycle.reverse()
        print("Eulerian cycle")
        print(" -> ".join((str(x) for x in eulirean_cycle)))


if __name__ == '__main__':
    main()
