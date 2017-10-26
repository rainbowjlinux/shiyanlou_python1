#!/usr/bin/env python3

############################
#File Name: poool.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-26 20:07:36
############################

from multiprocessing import Pool

def func(i):
    print(i)

if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(30):
        pool.apply(func, (i, ))
