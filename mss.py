import random
from timeit import default_timer as timer


def algorithm1(array):
    n = len(array)
    sub_low = 0
    sub_high = 0
    max_sum = 0

    for i in range(n):
        for j in range(i, n):
            total = 0
            for k in range(i, j + 1):
                total += array[k]
                if total > max_sum:
                    max_sum = total
                    sub_low = i
                    sub_high = j

    return max_sum, array[sub_low:sub_high + 1]


def algorithm2(array):
    n = len(array)
    sub_low = 0
    sub_high = 0
    max_sum = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += array[j]
            if total > max_sum:
                max_sum = total
                sub_low = i
                sub_high = j

    return max_sum, array[sub_low:sub_high + 1]


def runtime(runs, function_type):
    times = []
    n_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for i in range(len(n_sizes)):
        total = 0
        for j in range(runs):
            numbers = [random.randint(-50, 50) for k in range(n_sizes[i])]
            start = timer()
            function_type(numbers)
            end = timer()
            total += end - start
        average = total / runs
        times.append((n_sizes[i], average))
    return times


if __name__ == '__main__':
    print(runtime(10, algorithm1))
    print(runtime(10, algorithm2))
