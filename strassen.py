#!/usr/bin/env python3
import argparse
import math
import random
import pprint as pp

def create_matrix(size):
    d = {}
    for outer in range(size):
        for inner in range(size):
            if outer not in d:
                d[outer] = {}
            if inner not in  d[outer]:
                d[outer][inner] = int(random.random() * 50)
    return d

def populate_matrix(d):
    pass

def split_matrix(data, size):
    a, b, c, d = {}, {}, {}, {}
    hsize = int(size / 2)
    for outer in range(hsize):
        for inner in range(hsize):
            if outer not in a:
                a[outer] = {}
            if inner not in a[outer]:
                a[outer][inner] = data[outer][inner]
            if outer not in b:
                b[outer] = {}
            if inner not in b[outer]:
                b[outer][inner] = data[outer + hsize][inner]
            if outer not in c:
                c[outer] = {}
            if inner not in c[outer]:
                c[outer][inner] = data[outer][inner + hsize]
            if outer not in d:
                d[outer] = {}
            if inner not in d[outer]:
                d[outer][inner] = data[outer + hsize][inner + hsize]
    return a, b, c, d


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strassen Matrix Multiplier")
    parser.add_argument('-s', '--size', help='Size of the matrix', default=2, type=int)
    # parser.add_argument('-v', '--verbose', action='store_true', help='Show moves')
    args = parser.parse_args()
    size = args.size

    if math.log(size, 2) % 1 != 0:
        print("Matrix needs to be a power of 2")
        raise SystemExit

    m1 = create_matrix(size)
    m2 = create_matrix(size)
    pp.pprint(m1)
    pp.pprint(m2)
    a, b, c, d = split_matrix(m1, size)
    pp.pprint(a)
    pp.pprint(b)
    pp.pprint(c)
    pp.pprint(d)