#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    od_set1 = set_1 | set_2
    od_set2 = set_1 & set_2
    result = od_set1.difference(od_set2)
    return result
