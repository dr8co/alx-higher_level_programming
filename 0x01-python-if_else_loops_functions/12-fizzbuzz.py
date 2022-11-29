#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        tmp = ""
        if i % 3 == 0:
            tmp += "Fizz"
        if i % 5 == 0:
            tmp += "Buzz"
        elif i % 3 != 0:
            tmp += str(i)
        print("{:s}".format(tmp), end=' ')
