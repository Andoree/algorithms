def traverse_adjacency_list(adjacency_list, initial_edge, tmp_stack, final_stack, possible_ends, ):
    keep_going = True
    initial_node = initial_edge
    start_node = initial_node
    cycle_exists = True
    while keep_going:
        if len(adjacency_list[start_node]) > 0:
            tmp_stack.append(start_node)
            start_node = adjacency_list[start_node].pop()
        else:
            keep_going = False
            final_stack.append(start_node)
    if initial_node != start_node:
        possible_ends.append((initial_node, start_node))

    return cycle_exists


def find_towns_sequence(adjacency_list, nodes_with_no_input_edge):
    if len(nodes_with_no_input_edge) > 1:
        return [-1, ]
    elif len(nodes_with_no_input_edge) == 1:
        start_node = nodes_with_no_input_edge.pop()
    else:
        start_node = -1
        for i in range(len(adjacency_list)):
            if len(adjacency_list[i]) % 2 == 1:
                start_node = i
            elif len(adjacency_list[i]) > 1 and start_node == -1:
                start_node = i
                break

    tmp_stack = [start_node, ]
    final_stack = []
    possible_ends = []
    cycle_exists = True
    while len(tmp_stack) > 0 and cycle_exists:
        start_node = tmp_stack.pop()
        traverse_adjacency_list(adjacency_list, start_node, tmp_stack, final_stack, possible_ends)
    traversed_nodes_set = set(final_stack)
    if len(possible_ends) > 1:
        return [-1, ]
    else:
        if len(adjacency_list) == len(traversed_nodes_set):
            return final_stack
        else:
            return [-1, ]


def add_town_name(town_edge_name_mappings, town_start_id, town_end_id, town_name):
    names_list = town_edge_name_mappings[town_start_id].get(town_end_id)
    if names_list is None:
        town_edge_name_mappings[town_start_id][town_end_id] = []
    town_edge_name_mappings[town_start_id][town_end_id].append(town_name)


def main():
    with open("towns_input_bad.txt", 'r', encoding="utf-8") as inp_file:
        letters_set = set()
        letters_with_input_edge = set()
        for line in inp_file:
            town = line.strip()
            town_start = town[0].lower()
            town_end = town[-1].lower()
            letters_set.add(town_start)
            letters_set.add(town_end)
            letters_with_input_edge.add(town_end)
        inp_file.seek(0)
        letters_with_no_input_edge = letters_set.difference(letters_with_input_edge)
        id_to_letter = {i: letter for i, letter in enumerate(letters_set)}
        letter_to_id = {letter: i for i, letter in id_to_letter.items()}
        nodes_with_no_input_edge = set([letter_to_id[x] for x in letters_with_no_input_edge])
        adjacency_list = [[] for _ in range(len(letters_set))]
        town_edge_name_mappings = {letter_id: {} for letter_id in id_to_letter.keys()}
        for line in inp_file:
            town = line.strip()
            town_start_id = letter_to_id[town[0].lower()]
            town_end_id = letter_to_id[town[-1].lower()]
            adjacency_list[town_start_id].append(town_end_id)
            add_town_name(town_edge_name_mappings, town_start_id, town_end_id, town)
    towns_sequence = find_towns_sequence(adjacency_list, nodes_with_no_input_edge)
    if towns_sequence[0] == -1:
        print("No solution")
    else:
        towns_sequence.reverse()
        print("Solution exists:")
        print("Solution:")
        for i in range(len(towns_sequence) - 1):
            print(town_edge_name_mappings[towns_sequence[i]][towns_sequence[i + 1]].pop())


if __name__ == '__main__':
    main()
