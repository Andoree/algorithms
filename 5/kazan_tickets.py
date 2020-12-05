import time

import numpy as np

factorials_memory = [1]


def factorial(n):
    if len(factorials_memory) <= n:
        for i in range(len(factorials_memory), n + 1):
            factorials_memory.append(factorials_memory[i - 1] * i)

    return factorials_memory[n]


def is_integers_list_splitable(numbers_list: list):
    """
    Estimates whether a lsit of integers can be split into two
    subsets with equal sums
    :param numbers_list: List of integers
    :return: Boolean: Is a list of integers can be split into two
    subsets with equal sums of elements
    """
    list_length = len(numbers_list)
    list_sum = sum(numbers_list)

    if list_sum % 2 == 1:
        return False
    solution_matrix = np.empty(shape=(list_sum // 2 + 1, list_length + 1), dtype=np.bool)
    for i in range(solution_matrix.shape[1]):
        solution_matrix[0][i] = True
    for i in range(1, solution_matrix.shape[0]):
        solution_matrix[i][0] = False
    for i in range(1, solution_matrix.shape[0]):
        for j in range(1, solution_matrix.shape[1]):
            if i - numbers_list[j - 1] >= 0:
                solution_matrix[i][j] = solution_matrix[i][j - 1] or solution_matrix[i - numbers_list[j - 1]][j - 1]
            else:
                solution_matrix[i][j] = solution_matrix[i][j - 1]
    return solution_matrix[solution_matrix.shape[0] - 1][solution_matrix.shape[1] - 1]


def find_number_of_kazan_tickets(ticket_length):
    """
    Calculates the number of Kazan tickets of length ticket_length
    :param ticket_length: Length of tickets
    :return: Number of Kazan tickets of the given length
    """
    num_tickets = 0
    for num_0s in range(ticket_length + 1):
        for num_1s in range(ticket_length - num_0s + 1):
            for num_2s in range(ticket_length - (num_0s + num_1s) + 1):
                for num_3s in range(ticket_length - (num_0s + num_1s + num_2s) + 1):
                    for num_4s in range(ticket_length - (num_0s + num_1s + num_2s + num_3s) + 1):
                        for num_5s in range(ticket_length - (num_0s + num_1s + num_2s + num_3s + num_4s) + 1):
                            for num_6s in range(
                                    ticket_length - (num_0s + num_1s + num_2s + num_3s + num_4s + num_5s) + 1):
                                for num_7s in range(ticket_length - (
                                        num_0s + num_1s + num_2s + num_3s + num_4s + num_5s + num_6s) + 1):
                                    for num_8s in range(ticket_length - (
                                            num_0s + num_1s + num_2s + num_3s + num_4s + num_5s + num_6s + num_7s) + 1):
                                        ticket_digit_counts = [num_0s, num_1s, num_2s, num_3s, num_4s, num_5s,
                                                               num_6s, num_7s, num_8s, ]
                                        num_9s = max(ticket_length - sum(ticket_digit_counts), 0)
                                        ticket_digit_counts.append(num_9s)
                                        assert sum(ticket_digit_counts) == ticket_length
                                        ticket_digits = []
                                        for i in range(len(ticket_digit_counts)):
                                            ticket_digits.extend([i] * ticket_digit_counts[i])
                                        if is_integers_list_splitable(ticket_digits):
                                            num_permutations = factorial(ticket_length)
                                            for multiplicity in ticket_digit_counts:
                                                num_permutations = num_permutations // factorial(multiplicity)
                                            num_tickets += num_permutations
    return num_tickets


def main():
    ticket_length = int(input("Enter tickets length"))
    start_time = time.time()
    num_tickets = find_number_of_kazan_tickets(ticket_length)
    """
    499959437775564 - number of tickets
    400.02 - time elapsed(seconds)
    """
    print(num_tickets)
    print(f"{time.time() - start_time:.2f}")


if __name__ == '__main__':
    main()
