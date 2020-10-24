import numpy as np


def dijkstra_shortest_path(weighted_adjacency_matrix, start_vertex):
    num_vertices = weighted_adjacency_matrix.shape[0]
    path_costs = np.zeros(shape=num_vertices, dtype=np.float)
    previous_vertices = np.full(num_vertices, dtype=np.int, fill_value=-1)
    visits_stack = []
    visited_nodes_set = set()
    current_vertex = start_vertex
    previous_vertices[current_vertex] = current_vertex
    visits_stack.append(current_vertex)
    while len(visits_stack) > 0:
        current_vertex = visits_stack.pop()
        distances_from_current = [(i, dist) for i, dist in enumerate(weighted_adjacency_matrix[current_vertex])]
        distances_from_current.sort(key=lambda t: t[1])
        for vertex_id, dist in distances_from_current:
            if vertex_id not in visited_nodes_set:
                visited_nodes_set.add(vertex_id)
                visits_stack.append(vertex_id)
                previous_vertices[vertex_id] = current_vertex
                path_costs[vertex_id] = path_costs[current_vertex] + dist
                break

    return path_costs, previous_vertices


def adjacency_probabilities_to_log(weighted_adjacency_matrix, ):
    for i in range(len(weighted_adjacency_matrix)):
        for j in range(len(weighted_adjacency_matrix)):
            p = weighted_adjacency_matrix[i][j]
            if p == np.inf or p == 0:
                continue
            else:
                q = 1 - p
                minus_ln = np.log(q)
                weighted_adjacency_matrix[i][j] = minus_ln


def main():
    num_vertices = 7
    weighted_adjacency_matrix = np.full(shape=(num_vertices, num_vertices), fill_value=np.inf, dtype=np.float)
    adjacency_probabilities_to_log(weighted_adjacency_matrix)
    # weighted_adjacency_matrix[0][1] = 8
    # weighted_adjacency_matrix[0][2] = 2
    # weighted_adjacency_matrix[1][2] = 1
    # weighted_adjacency_matrix[1][4] = 6
    # weighted_adjacency_matrix[6][1] = 2
    # weighted_adjacency_matrix[2][6] = 3
    # weighted_adjacency_matrix[2][3] = 3
    # weighted_adjacency_matrix[3][6] = 1
    # weighted_adjacency_matrix[6][4] = 1
    # weighted_adjacency_matrix[4][5] = 2
    # weighted_adjacency_matrix[5][3] = 1
    for i in range(num_vertices):
        weighted_adjacency_matrix[i][i] = 0

    path_costs, previous_vertices = dijkstra_shortest_path(weighted_adjacency_matrix, 5)
    print("Path costs:")
    print(path_costs)
    print("Previous vertices")
    print(previous_vertices)


if __name__ == '__main__':
    main()
