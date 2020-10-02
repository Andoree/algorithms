import random


def integral_function(arguments_list):
    numerator = arguments_list[0]
    denominator = sum(arguments_list)
    return numerator / denominator


def main():
    num_variables = int(input("Введите число переменных:\n"))
    num_trials = int(input("Введите число испытаний:\n"))
    counter = 0

    for trial_id in range(num_trials):
        arguments_vector = [random.random() for i in range(num_variables)]
        function_value = integral_function(arguments_vector)
        random_value = random.random()
        if random_value < function_value:
            counter += 1
    approximate_solution = counter / num_trials
    print(f"Аналитическое решение: {1 / num_variables}")
    print(f"Решение Монте-Карло: {approximate_solution}")


if __name__ == '__main__':
    main()
