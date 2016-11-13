#!/usr/bin/env python3
import numpy
import math
import pprint as pp
import argparse

def create_matrix(m):
    """Function to create a random matrix in which values range from 1 to 20"""

    return [[numpy.random.randint(1,20) for a in range(m)] for t in range(m)]

def split_matrix(m):
    """Function to split the matrix into 4 equal quarters"""

    row_len = int(len(m[0][:]))
    col_len = int(len(m[:][0]))
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


def matrix_add(a,b):
    """Addition of two matrices"""

    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])
    if row_len_a == row_len_b and col_len_a == col_len_b:
        c = [[0 for i in range(col_len_a)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for j in range(col_len_a):
                c[i][j] = a[i][j] + b[i][j]
    return c

def matrix_subtract(a,b):
    """Subtraction of two matrices"""

    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])
    if row_len_a == row_len_b and col_len_a == col_len_b:
        c = [[0 for i in range(col_len_a)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for j in range(col_len_a):
                c[i][j] = a[i][j] - b[i][j]
    return c

def matrix_product(a,b):
    """Product of two matrices using the regular method."""

    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])

    if col_len_a == row_len_b:
        c = [[0 for i in range(col_len_b)] for j in range(row_len_a)]
        for i in range(row_len_a):
            for k in range(col_len_a):
                for j in range(col_len_b):
                    c[i][j] += a[i][k]*b[k][j]
    return c

def matrix_merge(a,b,c,d):

    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])
    row_len_c = len(c[0][:])
    col_len_c = len(c[:][0])
    row_len_d = len(d[0][:])
    col_len_d = len(d[:][0])

    result = [[0 for i in range(row_len_a + row_len_c)] for t in range(col_len_a + col_len_b)]

    if row_len_a == row_len_b and col_len_a == col_len_c and col_len_b == col_len_d and row_len_c == row_len_d:

        for i in range(row_len_a):
            for j in range(col_len_a):
                result[i][j] = a[i][j]

        for i in range(row_len_b):
            for j in range(col_len_b):
                result[i][j+col_len_a] = b[i][j]

        for i in range(row_len_c):
            for j in range(col_len_c):
                result[i+row_len_a][j] = c[i][j]

        for i in range(row_len_d):
            for j in range(col_len_d):
                result[i+row_len_a][j+col_len_a] = d[i][j]

    return result

def strassen_solution(a,b):
    row_len_a = len(a[1][:])
    col_len_a = len(a[:][1])
    row_len_b = len(b[1][:])
    col_len_b = len(b[:][1])

    """
    Checking condition for whether the rows and columns satisfy the condition to be split into 4 equal quarters.
    If condition is true, split the matrix and create the 10 sub matrices
    """
    if row_len_a == col_len_a and row_len_b == col_len_b and col_len_a == row_len_b and row_len_a % 2 == 0:
        a11,a12,a21,a22 = split_matrix(a)
        b11,b12,b21,b22 = split_matrix(b)
        s1 = matrix_subtract(b12,b22)
        s2 = matrix_add(a11,a12)
        s3 = matrix_add(a21,a22)
        s4 = matrix_subtract(b21,b11)
        s5 = matrix_add(a11,a22)
        s6 = matrix_add(b11,b22)
        s7 = matrix_subtract(a12,a22)
        s8 = matrix_add(b21,b22)
        s9 = matrix_subtract(a11,a21)
        s10 = matrix_add(b11,b12)

        """
        Implement the recursive condition. The base case is when the original matrix is of size 2.
        When it reaches the base case, multiplication is done using the regular method to ensure that
        the product is a 2D array. This ensures easy merging with the merge function
        """

        if row_len_a > 2:
            p1 = strassen_solution(a11,s1)
        else:
            p1 = matrix_product(a11,s1)
      
        if row_len_a > 2:
            p2 = strassen_solution(s2,b22)
        else:
            p2 = matrix_product(s2,b22)
       
        if row_len_a > 2:
            p3 = strassen_solution(s3,b11)
        else:
            p3 = matrix_product(s3,b11)
        
        if row_len_a > 2:
            p4 = strassen_solution(a22,s4)
        else:
            p4 = matrix_product(a22,s4)
        
        if row_len_a > 2:
            p5 = strassen_solution(s5,s6)
        else:
            p5 = matrix_product(s5,s6)
        
        if row_len_a > 2:
            p6 = strassen_solution(s7,s8)
        else:
            p6 = matrix_product(s7,s8)
        
        if row_len_a > 2:
            p7 = strassen_solution(s9,s10)
        else:
            p7 = matrix_product(s9,s10)

        c11 = matrix_add(matrix_add(p5,p6),matrix_subtract(p4,p2))
        c12 = matrix_add(p1,p2)
        c21 = matrix_add(p3,p4)
        c22 = matrix_subtract(matrix_add(p5,p1),matrix_add(p3,p7))


        return matrix_merge(c11,c12,c21,c22)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strassen Matrix Multiplier")
    parser.add_argument('-s', '--size', help='Size of the matrix', default=2, type=int)
    args = parser.parse_args()
    size = args.size

    if math.log(size, 2) % 1 != 0:
        print("Matrix needs to be a power of 2")
        raise SystemExit

    m1 = create_matrix(size)
    m2 = create_matrix(size)

    pp.pprint(m1)
    pp.pprint(m2)

    answer = strassen_solution(m1,m2)

    answer2 = matrix_product(m1,m2)

    pp.pprint(answer)
    pp.pprint(answer2)