import random
import csv
from timeit import default_timer as timer
from mss_algos import *


def runtime(runs, alg_type, n_sizes):
    times = []
    for i in range(len(n_sizes)):
        total = 0
        for j in range(runs):
            numbers = [random.randint(-50, 50) for k in range(n_sizes[i])]
            start = timer()
            alg_type(numbers)
            end = timer()
            total += end - start

        average = total / runs
        times.append((n_sizes[i], average))
    return times


def get_runtimes():
    a1_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    a2_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    a3_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    write_times('alg1_times.csv', runtime(10, algorithm1, a1_n))
    write_times('alg2_times.csv', runtime(10, algorithm2, a2_n))
    write_times('alg3_times.csv', runtime(10, algorithm3, a3_n))

    print('Wrote csv runtime files...')


def write_times(filename, array):
    with open(filename, 'wb') as output:
        file_writer = csv.writer(output)
        for row in array:
            file_writer.writerow(row)


if __name__ == '__main__':
    get_runtimes()
