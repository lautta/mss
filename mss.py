import random
from timeit import default_timer as timer


def algorithm1(array):
    n = len(array)
    start = 0
    end = 0
    max = 0

    for i in range(n):
        for j in range(i, n):
            total = 0
            for k in range(i, j + 1):
                total += array[k]
                if total > max:
                    max = total
                    start = i
                    end = j

    return max, array[start:end + 1]


def algorithm2(array):
    n = len(array)
    start = 0
    end = 0
    max = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += array[j]
            if total > max:
                max = total
                start = i
                end = j

    return max, array[start:end + 1]


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
