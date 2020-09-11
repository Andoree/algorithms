def calculate_n_th_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1

    for i in range(n):
        fib_n_minus_2 += fib_n_minus_1
        fib_n_minus_1 = fib_n_minus_1 ^ fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1 ^ fib_n_minus_2
        fib_n_minus_1 = fib_n_minus_1 ^ fib_n_minus_2
    return fib_n_minus_2



def main():
    while True:
        n = int(input('Введите номер числа Фибоначчи:\n'))
        if n == -1:
            break
        fib_n = calculate_n_th_fibonacci(n)
        print(f'Число фибоначчи: {fib_n}')

if __name__ == '__main__':
    main()

