import random


def find_numbers_split(numbers_array):
    array_sum = sum(numbers_array)
    if array_sum % 2 == 1:
        return None, None
    array_half_sum = array_sum // 2
    num_ones = 8
    for i in range(num_ones):
        numbers_array.remove(1)
    split_array_sum = 0
    for i in range(len(numbers_array)):
        if split_array_sum + numbers_array[i] >= array_half_sum:
            break
        else:
            split_array_sum += numbers_array[i]
    first_array_half = numbers_array[:i]
    second_array_half = numbers_array[i:]
    difference = array_half_sum - split_array_sum
    for i in range(difference):
        first_array_half.append(1)
    for i in range(num_ones - difference):
        second_array_half.append(1)
    for i in range(num_ones):
        numbers_array.append(1)

    return first_array_half, second_array_half


def main():
    sum_size = int(input("Ticker length:\n"))
    ticket_array = []
    for i in range(sum_size):
        ticket_digit = random.randint(0, 9)
        ticket_array.append(ticket_digit)
    first_array_half, second_array_half = find_numbers_split(ticket_array)
    if first_array_half is None:
        print("Ticket digits sum is odd. No solution")
    else:
        print(f"Sum of the whole array:\n{sum(ticket_array)}")
        print(f"Sum of the first array:\n{sum(first_array_half)}")
        print(f"Sum of the second array:\n{sum(second_array_half)}")
        print("Array lengths", len(first_array_half), len(second_array_half), len(ticket_array))


if __name__ == '__main__':
    main()
