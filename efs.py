#!/usr/bin/python
# -*- coding: utf-8 -*-
u'''
Sum of even Fibonacci numbers
'''

from sys import argv

def efs(limit):
    odd = 1
    even = 2
    current_sum = 3
    even_sum = 2
    while current_sum <= limit:
        if current_sum % 2 == 0:
            even_sum += current_sum
        odd = even
        even = current_sum
        current_sum = odd + even
    return even_sum

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: efs NUMBER'
        exit()
    try:
        number = int(argv[1])
    except ValueError:
        print 'Argument must be integer number'
        exit()
    if number < 1:
        print '%s less than first Fibonacci number' % number
        exit()
    print efs(number)