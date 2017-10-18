#!/usr/bin/env python3

def func1():
    global a
    a = 90
    print(a)

a = 9

def func2():
    a = 0
    print(a)

print("main a=", a)
print("call func1, a=", end='')
func1()
print("call func2, a=", end='')
func2()
print("main a=", a)
