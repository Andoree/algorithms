factorials_memory = [1]


def factorial(n):
    if len(factorials_memory) < n:
        for i in range(len(factorials_memory), n + 1):
            factorials_memory.append(factorials_memory[i - 1] * i)

    return factorials_memory[n]


def binomial_coefficient(n, k):
    n_factorial = factorial(n)
    k_factorial = factorial(k)
    n_minus_k_factorial = factorial(n - k)
    return n_factorial // (k_factorial * n_minus_k_factorial)


def calculate_failure_probability(num_trials, q):
    p = 1 - q
    n = num_trials // 2
    probability = 0
    for i in range(n + 1):
        pr = (p **(num_trials - i))* (q ** i) * binomial_coefficient(num_trials, i)
        probability += pr
    return probability


def main():
    file_length = 1000
    num_trials = 50
    q = 0.4
    print(binomial_coefficient(30, 2))
    print(calculate_failure_probability(num_trials, q))

    print(factorial(2))
    print(factorial(5))
    print(factorial(4))


if __name__ == '__main__':
    main()
