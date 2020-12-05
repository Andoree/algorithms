from collections import Counter
from random import randint

import numpy as np

FACTORIALS_MEMORY = [1]


def factorial(n):
    if len(FACTORIALS_MEMORY) <= n:
        for i in range(len(FACTORIALS_MEMORY), n + 1):
            FACTORIALS_MEMORY.append(FACTORIALS_MEMORY[i - 1] * i)
    return FACTORIALS_MEMORY[n]


def binomial_coefficient(n, k):
    n_factorial = factorial(n)
    k_factorial = factorial(k)
    n_minus_k_factorial = factorial(n - k)
    return n_factorial // (k_factorial * n_minus_k_factorial)


def calculate_failure_probability(num_trials, p):
    q = 1 - p
    n = num_trials // 2
    probability = 0
    for i in range(n + 1):
        pr = (p ** (num_trials - i)) * (q ** i) * binomial_coefficient(num_trials, i)
        probability += pr
    return 1 - probability


def main():
    file_length = int(input("Input file length:\n"))
    repeated_number = int(input("Input repeated number:\n"))
    repeated_number_proportion = float(input("Input repeated number proportion:\n"))
    epsilon = float(input("Input error probability:\n"))
    num_repeated = int(file_length * repeated_number_proportion)

    data_array = [repeated_number] * num_repeated
    data_array.extend([randint(0, 100) for i in range(file_length - num_repeated)])
    data_array = np.array(data_array)

    num_trials = 1
    error_probability = calculate_failure_probability(num_trials, repeated_number_proportion)
    while error_probability > epsilon:
        num_trials *= 2
        error_probability = calculate_failure_probability(num_trials, repeated_number_proportion)
    sampled_array = np.random.choice(data_array, size=num_trials)
    counter = Counter(sampled_array)
    probable_most_common_number, n_count = counter.most_common(1)[0]
    print(f"Most common number: {probable_most_common_number} ({n_count} / {num_trials})")
    print(f"Error probability: {error_probability}")



if __name__ == '__main__':
    main()
