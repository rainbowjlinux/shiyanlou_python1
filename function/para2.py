#!/usr/bin/env python3

def f(a, d=[]):
    print ("d=", d)
    d.append(a)
    return d
def f2():
    print ("f2")
    print (f(1))
    print (f(2, []))
    print (f(3))
def f3():
    print ("f3")
    print (f(4))

if __name__ == '__main__':
    f2()
    f3()
    f2()
    print("main")
    print(f(5))
