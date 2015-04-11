#!/usr/bin/env python

def solver(f):
    test_cases = int(f.readline())
    for i in xrange(0, test_cases):
        max_shy, shy_str = f.readline().split()
        friends_needed = calc_friends(int(max_shy), shy_str)
        print_solution(i + 1, friends_needed)

def print_solution(t, friends_needed):
    print "Case #{}: {}".format(t, friends_needed)

def calc_friends(max_shy, shy_str):
    friends_needed = 0
    stand_ups = 0
    for i in xrange(0, max_shy + 1):
        if shy_str[i] != '0':
            new_friends = max(0, i - stand_ups)
            friends_needed += new_friends
            stand_ups += int(shy_str[i]) + new_friends
    return friends_needed


if __name__ == '__main__':
    f = open('A-large.in', 'r')
    solver(f)
