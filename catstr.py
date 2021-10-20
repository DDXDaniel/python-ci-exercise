#coding: utf-8

import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("ArgsError: There is too much arguments!!\n")

    a = sys.argv[1]
    b = sys.argv[2]

    print(a + b)
