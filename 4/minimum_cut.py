import numpy as np
import random


class Edge:
    def __init__(self, node_1, node_2):
        self.old_node_1 = node_1
        self.old_node_2 = node_2
        self.current_node_1 = None
        self.current_node_2 = None


def squeeze_graph(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    not_squeezed_vertices = set((i for i in range(num_vertices)))

    for i in range(num_vertices - 2):
        chosen_vertices = random.sample(not_squeezed_vertices, 2)
        while adjacency_matrix[chosen_vertices[0]][chosen_vertices[1]] == 0:
            chosen_vertices = random.sample(not_squeezed_vertices, 2)
        new_vertex = chosen_vertices[0]
        squeezed_vertex = chosen_vertices[1]
        not_squeezed_vertices.remove(squeezed_vertex)
        for j in range(num_vertices):
            if adjacency_matrix[squeezed_vertex][j] > 1:
                edge_multiplicity = adjacency_matrix[squeezed_vertex][j]
                adjacency_matrix[squeezed_vertex][j] = 0
                adjacency_matrix[j][squeezed_vertex] = 0
                adjacency_matrix[new_vertex][j] += edge_multiplicity
                adjacency_matrix[j][new_vertex] += edge_multiplicity


def main():
    input_path = r'temp/10.txt'
    adjacency_lists = []
    with open(input_path, 'r', encoding="utf-8") as inp_file:
        line = inp_file.readline().strip()
        attrs = line.split()
        num_vertices, num_edges = int(attrs[0]), int(attrs[1])
        for i in range(num_vertices):
            line = inp_file.readline().strip()
            edge_multiplicities_list = [int(x) for x in line.split()]
            for node_id, node_multiplicity in enumerate(edge_multiplicities_list):
                pass
            adjacency_lists.append(edge_multiplicities_list)
        # print(input_list)
        adjacency_matrix = np.array(adjacency_lists)
    adjacency_matrix_copy = adjacency_matrix.copy()
    adjacency_matrix[0][0] = 100
    print(adjacency_matrix_copy)


if __name__ == '__main__':
    main()
