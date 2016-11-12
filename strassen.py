#!/usr/bin/env python3
import numpy
import math
import pprint as pp 

"""Function to create a random matrix in which values range from 1 to 20"""
def create_matrix(m):

    return [[numpy.random.randint(1,20) for a in range(m)] for t in range(m)]

"""Function to split the matrix into 4 equal quarters"""
def split_matrix(m):
    row_len = len(m[1][:])
    col_len = len(m[:][1])
    if row_len == col_len and row_len % 2 == 0:
        a = [[0 for i in range(row_len/2)] for j in range(col_len/2)]
        b = [[0 for i in range(row_len/2)] for j in range(col_len/2)]
        c = [[0 for i in range(row_len/2)] for j in range(col_len/2)]
        d = [[0 for i in range(row_len/2)] for j in range(col_len/2)]
        for i in range(row_len/2):
            for j in range(col_len/2):
                a[i][j] = m[i][j]
                b[i][j] = m[i][j+col_len/2]
                c[i][j] = m[i+row_len/2][j]
                d[i][j] = m[i+row_len/2][j+col_len/2]
    return a,b,c,d


"""Addition of two matrices"""
def matrix_add(a,b):
    row_len_a = len(a[1][:])
    col_len_a = len(a[:][1])
    row_len_b = len(b[1][:])
    col_len_b = len(b[:][1])
    if row_len_a == row_len_b and col_len_a == col_len_b:
        c = [[0 for i in range(col_len_a)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for j in range(col_len_a):
                c[i][j] = a[i][j] + b[i][j]
    return c

"""Subtraction of two matrices"""
def matrix_subtract(a,b):
    row_len_a = len(a[1][:])
    col_len_a = len(a[:][1])
    row_len_b = len(b[1][:])
    col_len_b = len(b[:][1])
    if row_len_a == row_len_b and col_len_a == col_len_b:
        c = [[0 for i in range(col_len_a)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for j in range(col_len_a):
                c[i][j] = a[i][j] - b[i][j]
    return c

"""Product of two matrices using the regular method. I don't think we'll be needing this, but I defined it just in case"""
def matrix_product(a,b):
    row_len_a = len(a[1][:])
    col_len_a = len(a[:][1])
    row_len_b = len(b[1][:])
    col_len_b = len(b[:][1])

    if col_len_a == row_len_b:
        c = [[0 for i in range(col_len_b)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for k in range(col_len_a):
                for j in range(col_len_b):
                    c[i][j] += a[i][k]*b[k][j]
    return c


def strassen_solution(a,b):
    row_len_a = len(a[1][:])
    col_len_a = len(a[:][1])
    row_len_b = len(b[1][:])
    col_len_b = len(b[:][1])

    if row_len_a == col_len_a and row_len_b == col_len_b and col_len_a == row_len_b and row_len_a % 2 == 0:
        a11,a12,a21,a22 = split_matrix(a)
        b11,b12,b21,b22 = split_matrix(b)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Strassen Matrix Multiplier")
#     parser.add_argument('-s', '--size', help='Size of the matrix', default=2, type=int)
#     # parser.add_argument('-v', '--verbose', action='store_true', help='Show moves')
#     args = parser.parse_args()
#     size = args.size

#     if math.log(size, 2) % 1 != 0:
#         print("Matrix needs to be a power of 2")
#         raise SystemExit
