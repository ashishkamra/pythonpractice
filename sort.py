#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 2017

@author: kamraa
"""
# sorts a given list of numbers in place
import random
from datetime import datetime

def my_sort(x):
    

def main():
    # generate a list of random numbers in a range
    x = random.sample(range(0,10000), 1000)
    x_copy = list(x)

    start_time = datetime.now()
    x.sort()
    end_time = datetime.now()

    print('python internal sorting time= '+str(end_time - start_time))

    start_time = datetime.now()
    mysort(x_copy)
    end_time = datetime.now()

    print('my sorting algo sorting time= '+str(end_time - start_time))

if __name__ == '__main__':
    main()
