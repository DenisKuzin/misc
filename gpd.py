#!/usr/bin/python
# -*- coding: utf-8 -*-
u'''
Greatest prime divisor
'''

from sys import argv

def gpd(number):
    divisor = 2 # First prime divisor to check
    while divisor ** 2 <= number:
        if not number % divisor:
            number /= divisor
        else:
            divisor += 1
    if number != 1:
        return number
    else:
        return divisor

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: gpd NUMBER'
        exit()
    try:
        number = int(argv[1])
    except ValueError:
        print 'Argument must be integer number'
        exit()
    if number < 2:
        print '%s doesnt have prime divisors' % number
        exit()
    print gpd(number)