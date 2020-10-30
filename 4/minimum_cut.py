import os
import random
from copy import deepcopy


class Edge:
    def __init__(self, vertex_1, vertex_2):
        self.old_vertex_1 = vertex_1
        self.old_vertex_2 = vertex_2
        self.current_vertex_1 = vertex_1
        self.current_vertex_2 = vertex_2

    def __str__(self):
        return f"{self.old_vertex_1},{self.old_vertex_2},{self.current_vertex_1},{self.current_vertex_2}"

    def __repr__(self):
        return self.__str__()



def squeeze_graph(adjacency_lists):
    num_vertices = len(adjacency_lists)
    not_squeezed_vertices = set((i for i in range(num_vertices)))

    for i in range(num_vertices - 2):
        chosen_vertex = random.choice(list(not_squeezed_vertices))
        while len(adjacency_lists[chosen_vertex]) == 0:
            chosen_vertex = random.choice(list(not_squeezed_vertices))
        chosen_edge = random.choice(adjacency_lists[chosen_vertex])
        new_vertex = chosen_edge.current_vertex_2
        squeezed_vertex = chosen_edge.current_vertex_1

        not_squeezed_vertices.remove(squeezed_vertex)
        if len(adjacency_lists[squeezed_vertex]) > 0:
            edges_list = [v for v in adjacency_lists[squeezed_vertex] if v.current_vertex_2 != new_vertex]
            for e in edges_list:
                e.current_vertex_1 = new_vertex
            adjacency_lists[squeezed_vertex] = []
            adjacency_lists[new_vertex].extend(edges_list)

        for k, adj_vertex_list in enumerate(adjacency_lists):
            for vertex in adj_vertex_list:
                if vertex.current_vertex_2 == squeezed_vertex:
                    vertex.current_vertex_2 = new_vertex
        for adj_vertex_list in adjacency_lists:
            for vertex in adj_vertex_list:
                if vertex.current_vertex_2 == vertex.current_vertex_1:
                    adj_vertex_list.remove(vertex)

    for adj_vertex_list in adjacency_lists:
        for vertex in adj_vertex_list:
            if vertex.current_vertex_2 == vertex.current_vertex_1:
                adj_vertex_list.remove(vertex)
    return adjacency_lists


def main():
    inputs_dir = r'temp/'
    for fname in os.listdir(inputs_dir):
        input_path = os.path.join(inputs_dir, fname)
        with open(input_path, 'r', encoding="utf-8") as inp_file:
            line = inp_file.readline().strip()
            attrs = line.split()
            num_vertices, num_edges = int(attrs[0]), int(attrs[1])
            adjacency_lists = [[] for _ in range(num_vertices)]
            for vertex_id_1 in range(num_vertices):
                line = inp_file.readline().strip()
                edge_multiplicities_list = [int(x) for x in line.split()]
                for vertex_id_2 in range(vertex_id_1 + 1, num_vertices):
                    node_multiplicity = edge_multiplicities_list[vertex_id_2]
                    for j in range(node_multiplicity):
                        edge = Edge(vertex_id_1, vertex_id_2)
                        adjacency_lists[vertex_id_1].append(edge)
        num_tries = num_vertices * 3

        minimum_cut_length = float('inf')
        minimum_cut_edges = []
        for i in range(num_tries):
            adjacency_lists_copy = deepcopy(adjacency_lists)
            counter = 0
            candidate_cut_edges = []
            minimum_cut_adj_list = squeeze_graph(adjacency_lists_copy)
            for adj_list in minimum_cut_adj_list:
                for v in adj_list:
                    counter += 1
                    candidate_cut_edges.append((v.old_vertex_1, v.old_vertex_2))

            if counter < minimum_cut_length:
                minimum_cut_edges = candidate_cut_edges
                minimum_cut_length = counter
        print(f"File: {fname}, Solution of size: {minimum_cut_length}")
        print(minimum_cut_edges)



if __name__ == '__main__':
    main()
