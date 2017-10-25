#!/usr/bin/env python3

############################
#File Name: lambda.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 14:31:55
############################

def double(x):
    return x * 2

def use_anonymous_func(x, func):
    return func(x)

if __name__ == '__main__':
    x = 2
    print('use def function')
    print(double(x))

    an_double = lambda x: x * 2
    print('use anonymous function')
    print(an_double(x))

    print('use lambda for param')
    print(use_anonymous_func(x, lambda x: x * 2))
