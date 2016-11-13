#!/usr/bin/env python3
import numpy
import math
import pprint as pp
import argparse

def create_matrix(m):
    """Function to create a random matrix in which values range from 1 to 20"""

    if args.verbose:
        print("Creating Array with random ints in range from 1 through 20.")
    return [[numpy.random.randint(1,20) for a in range(m)] for t in range(m)]


def split_matrix(m):
    """Function to split the matrix into 4 equal quarters"""


    row_len = len(m[0][:])
    col_len = len(m[:][0])
    half_row_len = row_len // 2
    half_col_len = col_len // 2
    if args.verbose:
        print("Splitting a {}x{} matrix {} into quarters.".format(row_len, col_len, id(m)))

    if row_len == col_len and row_len % 2 == 0:
        a = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        b = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        c = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        d = [[0 for i in range(half_row_len)] for j in range(half_col_len)]
        for i in range(half_row_len):
            for j in range(half_col_len):
                a[i][j] = m[i][j]
                b[i][j] = m[i][j+half_col_len]
                c[i][j] = m[i+half_row_len][j]
                d[i][j] = m[i+half_row_len][j+half_col_len]
    if args.verbose:
        print("Produced matrices {}, {}, {}, and {} by splitting.".format(id(a), id(b), id(c), id(d)))
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
    if args.verbose:
        print("Creating a {}x{} matrix {} by summing matrices {} and {}.".format(row_len_a, col_len_a, id(c), id(a), id(b)))
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
    if args.verbose:
        print("Creating a {}x{} matrix {} by subtracting matrix {} from {}.".format(row_len_a, col_len_a, id(c), id(b), id(a)))
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
    if args.verbose:
        print("Creating a {}x{} matrix {} by multiplying matrices {} and {}.".format(row_len_a, col_len_a, id(c), id(b), id(a)))
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
    if args.verbose:
        print("Merged four matrices into new matrix {}.".format(id(result)))
    return result

def strassen_solution(a,b):
    row_len_a = len(a[0][:])
    col_len_a = len(a[:][0])
    row_len_b = len(b[0][:])
    col_len_b = len(b[:][0])

    """
    Checking condition for whether the rows and columns satisfy the condition to be split into 4 equal quarters.
    If condition is true, split the matrix and create the 10 sub matrices
    """
    if row_len_a == col_len_a and row_len_b == col_len_b and col_len_a == row_len_b and row_len_a % 2 == 0:
        if args.verbose:
            print("Entering main Strassen algorithm.")
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

    else:
        if args.verbose:
            print("Unable to perform Strassen. Performing standard matrix multiplication")
        c = matrix_product(a,b)
        return c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strassen Matrix Multiplier")
    parser.add_argument('-s', '--size', help='Size of the matrix', default=4, type=int)
    parser.add_argument('-v', '--verbose', help='Increase Verbosity', action='store_true')
    args = parser.parse_args()
    size = args.size

    m1 = create_matrix(size)
    m2 = create_matrix(size)

    print("Matrix 1 ({}x{}):".format(size, size))
    pp.pprint(m1)
    print("\nMatrix 2 ({}x{}):".format(size, size))
    pp.pprint(m2)

    strassen_answer = strassen_solution(m1, m2)
    traditional_answer = matrix_product(m1, m2)

    print("\nStrassen Product:")
    pp.pprint(strassen_answer)
    print("\nTraditional Product:")
    pp.pprint(traditional_answer)
