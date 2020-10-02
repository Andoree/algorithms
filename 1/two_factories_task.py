import numpy as np


def main():
    a_0 = [9, 9, 3, 4, 8, 7]
    # a_0 = [int(x) for x in input
    #     ("Введите стоимости путей нулевой страны:\n")]
    n = len(a_0)
    a_1 = [12, 5, 6, 4, 5, 9]
    # a_1 = [int(x) for x in input
    #     ("Введите стоимости путей первой страны:\n")]
    f_0_1 = [2, 3, 1, 3, 4, ]
    # f_0_1 = [int(x) for x in input
    #     ("Введите стоимости переходов из нулевой страны в первую:\n")]
    f_1_0 = [2, 1, 2, 2, 1, ]
    # f_1_0 = [int(x) for x in input
    #     ("Введите стоимости переходов из первой страны в нулевую:\n")]
    b_0 = np.zeros(shape=n, dtype=np.bool)
    b_1 = np.zeros(shape=n, dtype=np.bool)

    c_0_list = []
    c_1_list = []
    forward_pass_costs = [a_0, a_1]
    change_path_costs = [f_0_1, f_1_0]
    change_path_flags = [b_0, b_1]
    aggregated_costs = [c_0_list, c_1_list]
    # Forward pass, заполняем массивы решения
    for i in range(0, n):
        for j in range(2):
            if i == 0:
                aggregated_costs[j].append(forward_pass_costs[j][i])
            else:
                forward_cost = aggregated_costs[j][i - 1] + forward_pass_costs[j][i]
                round_cost = aggregated_costs[(j + 1) % 2][i - 1] + \
                             change_path_costs[(j + 1) % 2][i - 1] + forward_pass_costs[j][i]
                min_cost = min(forward_cost, round_cost)
                aggregated_costs[j].append(min_cost)
                change_path_flags[j][i] = True if round_cost < forward_cost else 0

    # Backward pass, восстанавливаем маршрут и стоимости
    optimal_path = []
    initial_node = 0 if aggregated_costs[0][-1] < aggregated_costs[1][-1] else 1
    optimal_path.append((initial_node, -1, 0))
    for i in range(n - 1, -1, -1):
        optimal_path.append((initial_node, initial_node, forward_pass_costs[initial_node][i]))
        if change_path_flags[initial_node][i] == True:
            previous_node = (initial_node + 1) % 2
            cost = change_path_costs[previous_node][i - 1]
            optimal_path.append((previous_node, initial_node, cost))
            initial_node = previous_node
    optimal_path.append((-1, initial_node, forward_pass_costs[initial_node][0]))
    optimal_path.reverse()
    for (from_node, to_node, cost) in optimal_path:
        if to_node == -1:
            print(f"End: {from_node}")
        elif from_node == -1:
            print(f"Start: {to_node}")
        elif from_node != to_node:
            print(f"Change path: {from_node} -> {to_node} (+ {cost} cost)")
        else:
            print(f"Go forward: {from_node} -> {to_node} (+ {cost} cost)")


if __name__ == '__main__':
    main()
