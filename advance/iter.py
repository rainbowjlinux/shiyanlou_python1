#!/usr/bin/env python3

############################
#File Name: iter.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 16:39:27
############################

if __name__== '__main__':
    l = [1,2,3,4]
    print('use for in...:')
    for x in l:
        print(x)

    print('use iter,next:')
    it = iter(l)
    print (next(it))
    print (next(it))
    print (next(it))
    print (next(it))

    print('other style,__iter__,__next__:')
    it = l.__iter__()
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())

    #list comprehension
    l = [x**x for x in range(1,4)]

    #generator
    g = (x**x for x in range(1,4))
    print(type(l))
    print(type(g))
    print('iter l:')
    for x in l:
        print (x)
    print('iter l:')
    for x in l:
        print (x)
    print('iter g:')
    for x in g:
        print (x)
    print('iter g:')
    for x in g:
        print (x)

