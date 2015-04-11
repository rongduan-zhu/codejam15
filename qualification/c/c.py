#!/usr/bin/env python
import sys

lookup = {
    '': '',
    '-': '-',
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
        solution = can_split(base_str * int(repeat), int(strlen))
        print_solution(i + 1, solution)

def print_solution(t, solution):
    print 'Case #{}: {}'.format(t, solution)

def can_split(repeated_str, strlen):
    if len(repeated_str) < 3:
        return 'NO'
    elif len(repeated_str) == 3:
        return 'YES' if repeated_str == 'ijk' else "NO"
    else:
        str_len = len(repeated_str)
        for i in xrange(1, str_len - 2):
            if get_x(repeated_str[:i], 'i', strlen):
                for j in xrange(i + 1, str_len - 1):
                    if get_x(repeated_str[i:j], 'j', strlen):
                        if get_x(repeated_str[j:], 'k', strlen):
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

def get_x(substr, x, strlen):
    multiple = len(substr) / strlen
    remainder = len(substr) % strlen

    combined = get_combined(substr[:strlen])

    if len(combined) and combined[0] == '-' and (not (multiple & 1)):
        combined = combined[1:]

    if multiple and remainder:
        remainder_combined = get_combined(substr[:remainder])
        combined = get_combined(add_str(combined, remainder_combined))

    return combined == x

def add_str(str1, str2):
    if len(str1) and len(str2) and str1[0] == '-' and str2[0] == '-':
        return str1[1:] + str2[1:]
    elif len(str2) and str2[0] == '-':
        return '-' + str1 + str2[1:]
    return str1 + str2


if __name__ == '__main__':
    f_name = sys.argv[1]
    f = open(f_name, 'r')
    solver(f)
