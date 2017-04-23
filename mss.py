# MSS correctness tests with file read/write

from mss_algos import *


def read_problems(filename):
    problems = []
    with open(filename, 'r') as input:
        for line in input:
            problem = [int(number) for number in line.strip().split()]
            problems.append(problem)
    print('Read %s file...' % filename)
    return problems


def write_results(filename, algo_func, algo_name, array, write_option):
    with open(filename, write_option) as output:
        output.write('Results for %s \n' % algo_name)
        for input in array:
            output.write('Input Array: [' + ', '.join([str(i) for i in input]) + ']\n')
            mss_results = algo_func(input)
            output.write('Max Sum: %s \nMax Sum Subarray: %s \n\n' % mss_results)
        output.write('\n\n')


if __name__ == '__main__':
    input_file = 'MSS_Problems.txt'
    output_file = 'MSS_Results.txt'

    read_arrays = read_problems(input_file)
    write_results(output_file, algorithm1, 'Enumeration', read_arrays, 'wb')
    write_results(output_file, algorithm2, 'Better Enumeration', read_arrays, 'ab')
    write_results(output_file, algorithm3, 'Divide-And-Conquer', read_arrays, 'ab')
    write_results(output_file, algorithm4, 'Linear-time', read_arrays, 'ab')

    print('Wrote %s file...' % output_file)
