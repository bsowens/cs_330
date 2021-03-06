# File: PseudoPolyNumberPartition.py
# Author: Nicholas Louie (nlouie@bu.edu), Jennifer Tsui (jgtsui@bu.edu)
# Date: 3/30/16
# Boston University Computer Science Spring 2016
# CS330 Assignment 5 Question 4 (b)
# Description: Solves the number partition problem with the Karmarkar-Karp Algorithm
# Resources: https://en.wikipedia.org/wiki/Partition_problem
# https://docs.python.org/3.0/library/heapq.html

import math
import heapq

# INPUT
test_list = [10, 8, 7, 6, 5]

# partition takes a list of integers and performs KK number partitioning algorithm

def karmarkar_karp(l):
    n = len(l)
    K = sum(l)

    # init heap, but since heappop only pops the min value, we will multiply each input value by -1
    heap = []
    for item in l:
        heapq.heappush(heap, item * -1)
    heapq.heapify(heap)

    while len(heap) > 1:
        i = heapq.heappop(heap)
        j = heapq.heappop(heap)
        heapq.heappush(heap, abs(i - j) * -1)
    # the result should be the residue. Switch negative sign back.
    return heapq.heappop(heap) * -1

# run example

#print("Running example list:", test_list)
#print(karmarkar_karp(test_list))
