#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = list(a_dictionary.keys())
    sorted_dict.sort()
    for key in sorted_dict:
        print("{}: {}".format(key, a_dictionary[key]))
