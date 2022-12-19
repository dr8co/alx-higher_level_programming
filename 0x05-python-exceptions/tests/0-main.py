#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

list_l = [3, 9, 1, 84, 7]

dummy = safe_print_list(list_l, 2)
print("nb_print: {:d}".format(dummy))
dummy = safe_print_list(list_l, len(list_l))
print("nb_print: {:d}".format(dummy))
dummy = safe_print_list(list_l, len(list_l) + 2)
print("nb_print: {:d}".format(dummy))
