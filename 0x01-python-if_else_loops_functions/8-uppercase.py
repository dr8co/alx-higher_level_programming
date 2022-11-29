#!/usr/bin/python3

def uppercase(str):
    tmp = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            tmp += chr(ord(c) - 32)
        else:
            tmp += c
    print("{:s}".format(tmp))
