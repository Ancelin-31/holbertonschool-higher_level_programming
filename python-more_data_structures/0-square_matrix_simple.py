#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    def square_list(lst):
        new_list = list(map(lambda i: i ** 2, lst))
        return new_list

    new_matrix = list(map(square_list, matrix))
    return new_matrix
