def return_num_tries(num_floors, num_balls):
    memory_array = [1] * num_balls
    num_steps = 1
    while True:
        num_steps += 1
        fixed_tries_array = []
        for i in range(num_balls):
            if i == 0:
                max_num_floors = memory_array[i] + 1
            else:
                max_num_floors = memory_array[i - 1] + memory_array[i] + 1
            fixed_tries_array.append(max_num_floors)
            if max_num_floors >= num_floors:
                return num_steps
        memory_array = fixed_tries_array


def main():
    num_floors = int(input("Number of floors:\n"))
    num_balls = int(input("Number of balls:\n"))
    solution = return_num_tries(num_floors, num_balls)
    print(f"Needed number of tries: {solution}")


if __name__ == '__main__':
    main()
