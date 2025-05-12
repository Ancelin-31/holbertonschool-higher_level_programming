#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for i, element in enumerate(row):
            if i < len(row) - 1:
                print("{}".format(element), end=" ")
            else:
                print("{}".format(element), end="")
        print("$")
