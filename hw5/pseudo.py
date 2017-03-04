# File: PseudoPolyNumberPartition.java
# Author: Nicholas Louie (nlouie@bu.edu), Jennifer Tsui (jgtsui@bu.edu)
# Date: 3/30/16
# Boston University Computer Science Spring 2016
# CS330 Assignment 5 Question 4 (a)
# Description: Solves the number partition problem in pseudopolynomial time.
# This class implements a dynamic programming algorithm that runs in time
# polynomial in n and B.
# Resources: https://en.wikipedia.org/wiki/Partition_problem

import math

# INPUT
test_list = [3, 1, 1, 2, 2, 1]
test_list_2 = [1,5]
test_list_3 = [1,1,4]

# partition takes a list of integers and performs the number partitioning algorithm


def partition(l):

    n = len(l)
    K = sum(l)


    # case where n = 2
    if n == 2:
        o = [-1,1]
        #print(o)
        return o
    # case where n = 3
    elif n == 3:
        o = [0,0,0]
        min_index = l.index(min(l))
        max_index = l.index(max(l))
        o[min_index] = -1
        o[max_index] = 1
        for i in range(len(l)):
            if not (i == max_index or i == min_index):
                if l[i] + min(l) < max(l):
                    o[i] = -1
                else:
                    o[i] = 1
        #print(o)
        return o
    else:
        # create a 2D array representation
        P = [[0 for x in range(n + 1)] for x in range(math.floor(K / 2) + 1)]

        # initialize leftmost column except for P(0,0) to false
        for i in range(math.floor(K / 2) + 1):
            P[i][0] = -1

        # initialize top row to true
        P[0] = [1 for x in range(len(P[0]))]

        # iterate through the 2D array
        for i in range(math.floor(K / 2) + 1):
            for j in range(n + 1):
                if i >= 1 and j >= 1:
                    if P[i][j-1] == 1 or P[i - l[j - 1]][j - 1] == 1:
                        # set to true
                        P[i][j] = 1
                    else:
                        P[i][j] = -1
        # take last row
        #print(P)
        l2 = P[math.floor(K/2)]
        # take first n elements.
        l3 = l2[:n]
        #print(l3)
        return l3

# run example
#print("Running example list:", test_list_3)
#partition(test_list_3)
