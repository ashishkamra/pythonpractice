#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:54:21 2017

@author: kamraa
"""
import random
def main():
    x = random.sample(range(0,100), 10)
    x.sort()
    #print(x)
    sum = 50
    i = 0
    j = len(x) - 1
    while i < j:
        test_sum = x[i] + x[j]

        if test_sum == sum:
            print('sum='+str(sum)+' x[i]='+str(x[i])+' x[j]='+str(x[j]))
            return 0

        if test_sum < sum:
            i += 1
        elif test_sum > sum:
            j -= 1
    print('did not find any numbers equal to the sum='+str(sum))
    return -1

if __name__ == '__main__':
  main()
