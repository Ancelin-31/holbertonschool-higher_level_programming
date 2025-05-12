#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) > 0:
        ta0 = tuple_a[0]
    else:
        ta0 = 0
    if len(tuple_a) > 1:
        ta1 = tuple_a[1]
    else:
        ta1 = 0

    if len(tuple_b) > 0:
        tb0 = tuple_b[0]
    else:
        tb0 = 0
    if len(tuple_b) > 1:
        tb1 = tuple_b[1]
    else:
        tb1 = 0

    new_tuple = (ta0 + tb0, ta1 + tb1)
    return new_tuple
