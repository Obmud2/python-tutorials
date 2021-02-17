#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:34:02 2019

@author: Jon
"""

def genPrime():
    
    primes = []
    next = 1
    while True:
        next += 1
        for i in primes:
            if next % i == 0:
                break
        else:
            primes.append(next)
            yield next

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
                