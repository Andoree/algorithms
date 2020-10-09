def traverse_adjacency_list(adjacency_list, initial_node, tmp_stack, possible_ends,):
    keep_going = True
    start_node = initial_node
    can_add_node = True
    cycle_exists = True
    while keep_going:
        if len(adjacency_list[start_node]) > 0:
            tmp_stack.append(start_node)
            start_node = adjacency_list[start_node].pop()
        else:
            keep_going = False
    if initial_node != start_node:
        possible_ends.append((initial_node, start_node))

    return cycle_exists


def find_towns_sequence(adjacency_list, nodes_with_no_input_edge):
    if len(nodes_with_no_input_edge) > 1:
        print('here f')
        return [-1, ]
    elif len(nodes_with_no_input_edge) == 1:
        start_node = nodes_with_no_input_edge.pop()
    else:
        for i in range(len(adjacency_list)):
            if len(adjacency_list[i]) % 2 == 1:
                start_node = adjacency_list[i][0]
                print(start_node)
                break

    print('AAAAAAAAA', start_node)
    tmp_stack = [start_node, ]
    final_stack = []
    possible_ends = []
    cycle_exists = True
    while len(tmp_stack) > 0 and cycle_exists:
        start_node = tmp_stack.pop()
        traverse_adjacency_list(adjacency_list, start_node, tmp_stack, possible_ends)
        final_stack.append(start_node)
    print('CYCLE EXISTS', cycle_exists)
    print(possible_ends)
    print(final_stack)

    traversed_nodes_set = set(final_stack)
    if len(possible_ends) > 1:
        print(possible_ends)
        print(len(possible_ends))
        print('here a')
        return [-1, ]
    else:
        print('gdsgsda', possible_ends)
        traversed_nodes_set.add(possible_ends[0][1])
        final_stack.insert(0, possible_ends[0][1])
        print(final_stack)
        if len(adjacency_list) == len(traversed_nodes_set):
            if len(possible_ends) == 0:
                return final_stack[:-1]
            else:
                print(possible_ends)
                print(final_stack)
                print(traversed_nodes_set)
                print('here d')
                return final_stack
        else:
            print('--' * 10)
            print(possible_ends)
            print(len(adjacency_list))
            print(len(traversed_nodes_set))
            print('--')
            print(adjacency_list)
            print(traversed_nodes_set)
            print('here e')
            return [-1, ]


def main():
    with open("towns_input.txt", 'r', encoding="utf-8") as inp_file:
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
        print('--')
        print(nodes_with_no_input_edge)
        print(letters_with_no_input_edge)
        print(id_to_letter)
        adjacency_list = [[] for _ in range(len(letters_set))]
        for line in inp_file:
            town = line.strip()
            town_start_id = letter_to_id[town[0].lower()]
            town_end_id = letter_to_id[town[-1].lower()]
            adjacency_list[town_start_id].append(town_end_id)
    print('aa', id_to_letter)
    print(adjacency_list)
    towns_sequence = find_towns_sequence(adjacency_list, nodes_with_no_input_edge)
    if towns_sequence[0] == -1:
        print("No solution")
    else:
        towns_sequence.reverse()
        print("Solution exists:")
        print("Solution:")
        print(" -> ".join((str(t) for t in towns_sequence)))


if __name__ == '__main__':
    main()
