#!/usr/bin/env python3

def countchar(str):
    char_set = set(str)
    for c in char_set:
        print (c, str.count(c))

if __name__ == '__main__':
    s = input("Input a string:")
    countchar(s)
