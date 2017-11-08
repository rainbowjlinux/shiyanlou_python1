#!/usr/bin/env python3

############################
#File Name: decrator.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 17:18:00
############################

class A(object):
    def foo(self, x):
        print("self:", self)

    @classmethod
    def cls_foo(cls, x):
        print("cls:", cls)

    @staticmethod
    def stc_foo(x):
        print("stc_foo:", x)

def main():
    a = A()
    a.foo('x')
    a.cls_foo('x')
    a.stc_foo('x')
    print('\nmethod:', a.foo)
    print('method:', a.cls_foo)
    print('method:', a.stc_foo)

    print("\nUse class to call function foo")
    #A.foo('x')
    A.foo(a, 'x')
    A.cls_foo('x')
    A.stc_foo('x')

if __name__ == '__main__':
    main()
