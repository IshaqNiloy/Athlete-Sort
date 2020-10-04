#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sorted_list = sorted(arr, key = lambda arr: arr[k])#Sorts the list by the k-th element of the list
    
    for item in sorted_list:
        for element in item:
            print(element, end = ' ')
        print()#Prints a new line 