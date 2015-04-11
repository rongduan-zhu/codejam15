#!/usr/bin/env python
import sys

def solver(f):
    test_cases = int(f.readline())
    for i in xrange(0, test_cases):
        num_people = int(f.readline())
        plates = map(int, f.readline().split())
        min_time = get_min_time(plates)
        print_solution(i + 1, min_time)

def print_solution(t, solution):
    print 'Case #{}: {}'.format(t, solution)

def get_min_time(plates):
    plates.sort()
    time_taken = 0
    min_time = plates[-1]
    while True:
        largest = plates.pop()
        splitted_1, splitted_2 = split_even(largest)
        plates.append(splitted_1)
        plates.append(splitted_2)
        plates.sort()

        min_time = min(time_taken + largest, min_time)
        time_taken += 1

        if largest == 1:
            return min_time

def split_even(num):
    half = num / 2
    if num & 1:
        return half, half + 1
    return half, half


if __name__ == '__main__':
    f_name = sys.argv[1]
    f = open(f_name, 'r')
    solver(f)
