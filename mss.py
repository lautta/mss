import random
import csv
from timeit import default_timer as timer


# algorithm 1
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


# algorithm 2
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


# helper function for algorithm 3
def maxSuffix(array, start, end):
    sum = array[end]
    maxSum = array[end]
    value = end

    for i in range(1, (end - start + 1)):
        sum += array[end - i]
        if sum > maxSum:
            maxSum = sum
            value = end - i
    return (maxSum, value)


# helper function for algorithm 3
def maxPrefix(array, start, end):
    sum = array[start]
    maxSum = array[start]
    value = start

    for i in range(1, (end - start + 1)):
        sum += array[start + i]
        if sum > maxSum:
            maxSum = sum
            value = start + i
    return (maxSum, value)


# algorithm 3
# returns the max subarray sum, the start index of the subarray, and the ending index of the subarray
def algorithm3(array, start, end):
    if start == end:
        return (array[start], start, end)

    mid = (end + start) / 2
    L_sum, L_start, L_end = algorithm3(array, start, mid)
    R_sum, R_start, R_end = algorithm3(array, mid + 1, end)

    suf_sum, suf_start = maxSuffix(array, start, mid)
    pref_sum, pref_end = maxPrefix(array, mid + 1, end)

    if L_sum > R_sum:
        if L_sum > (suf_sum + pref_sum):
            return (L_sum, L_start, L_end)
        else:
            return ((suf_sum + pref_sum), suf_start, pref_end)
    else:
        if R_sum > (suf_sum + pref_sum):
            return (R_sum, R_start, R_end)
        else:
            return ((suf_sum + pref_sum), suf_start, pref_end)


def runtime(runs, function_type, n_sizes):
    times = []
    for i in range(len(n_sizes)):
        total = 0
        for j in range(runs):
            numbers = [random.randint(-50, 50) for k in range(n_sizes[i])]

            # algorithm 3 requires 3 parameters
            if function_type == algorithm3:
                start = timer()
                function_type(numbers, 0, len(numbers) - 1)
                end = timer()
                total += end - start

            # algorithms 1 and 2 require 1 parameter
            else:
                start = timer()
                function_type(numbers)
                end = timer()
                total += end - start

        average = total / runs
        times.append((n_sizes[i], average))
    return times


def get_runtimes():
    a1_n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    a2_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    a3_n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    write_times('alg1_times.csv', runtime(10, algorithm1, a1_n))
    write_times('alg2_times.csv', runtime(10, algorithm2, a2_n))
    write_times('alg3_times.csv', runtime(10, algorithm3, a3_n))


def write_times(filename, array):
    with open(filename, 'wb') as output:
        file_writer = csv.writer(output)
        for row in array:
            file_writer.writerow(row)


def read_problems(filename):
    problems = []
    with open(filename, 'r') as input:
        for line in input:
            problem = [int(number) for number in line.strip().split()]
            problems.append(problem)
    return problems

if __name__ == '__main__':
    print(read_problems('MSS_Problems.txt'))
    get_runtimes()
