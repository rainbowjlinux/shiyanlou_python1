#!/usr/bin/env python3

############################
#File Name: sync.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-26 11:06:46
############################

from multiprocessing import Process, Value
import time, os

def func(val):
    for i in range(5):
        val.value += 1
        print(os.getpid(),':',v.value)
        time.sleep(0.01)

if __name__ == '__main__':
    v = Value('i', 0)
    p10 = [Process(target=func, args=(v, )) for x in range(5)]
    for p in p10:
        p.start()
    for p in p10:
        p.join()
        print('parent:',v.value)
    print('value:',v.value)
