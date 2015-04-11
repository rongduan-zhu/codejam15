#!/usr/bin/env python
import sys

lookup = {
    '': '',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'ii': '-',
    'ij': 'k',
    'ik': '-j',
    'ji': '-k',
    'jj': '-',
    'jk': 'i',
    'ki': 'j',
    'kj': '-i',
    'kk': '-'
}

def solver(f):
    test_cases = int(f.readline())
    for i in xrange(0, test_cases):
        strlen, repeat = f.readline().split()
        base_str = f.readline().rstrip()
        solution = can_split(base_str * int(repeat))
        print_solution(i + 1, solution)

def print_solution(t, solution):
    print 'Case #{}: {}'.format(t, solution)

def can_split(repeated_str):
    if len(repeated_str) < 3:
        return 'NO'
    elif len(repeated_str) == 3:
        return 'YES' if repeated_str == 'ijk' else "NO"
    else:
        str_len = len(repeated_str)
        for i in xrange(1, str_len - 2):
            if get_x(repeated_str[:i], 'i'):
                for j in xrange(i + 1, str_len - 1):
                    if get_x(repeated_str[i:j], 'j'):
                        if get_x(repeated_str[j:], 'k'):
                            return "YES"
        return "NO"

def get_combined(substr):
    if substr in lookup:
        return lookup[substr]

    subsubstr = get_combined(substr[:-1])
    if len(subsubstr) and subsubstr[0] == '-':
        subsubstr_combined = lookup[subsubstr[1:] + substr[-1]]
        if subsubstr_combined[0] == '-':
            lookup[substr] = subsubstr_combined[1:]
            return lookup[substr]
        else:
            lookup[substr] = '-' + subsubstr_combined
            return lookup[substr]
    else:
        subsubstr_combined = lookup[subsubstr + substr[-1]]
        lookup[substr] = subsubstr_combined
        return lookup[substr]

def get_x(substr, x):
    combined = get_combined(substr)
    return combined == x

if __name__ == '__main__':
    f_name = sys.argv[1]
    f = open(f_name, 'r')
    solver(f)
