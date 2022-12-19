#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
printed = safe_print_integer(value)
if not printed:
    print("{} is not an integer".format(value))

value = -89
printed = safe_print_integer(value)
if not printed:
    print("{} is not an integer".format(value))

value = "School"
printed = safe_print_integer(value)
if not printed:
    print("{} is not an integer".format(value))
