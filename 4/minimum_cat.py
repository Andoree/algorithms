import numpy as np
import random

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
    input_list = []
    with open(input_path, 'r', encoding="utf-8") as inp_file:
        line = inp_file.readline().strip()
        attrs = line.split()
        num_vertices, num_edges = int(attrs[0]), int(attrs[1])
        for i in range(num_vertices):
            line = inp_file.readline().strip()
            edges = [int(x) for x in line.split()]
            input_list.append(edges)
        # print(input_list)
        adjacency_matrix = np.array(input_list)
    adjacency_matrix_copy = adjacency_matrix.copy()
    adjacency_matrix[0][0] = 100
    print(adjacency_matrix_copy)







if __name__ == '__main__':
    main()