#!/usr/bin/env python3

############################
#File Name: sync.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-26 11:06:46
############################

from multiprocessing import Process, Value, Lock
import time, os

def func(val, lock):
    for i in range(50):
        time.sleep(0.01)
        '''
        with lock:
            val.value += 1
        '''
        lock.acquire()
        val.value += 1
        lock.release()
        print(os.getpid(),':',v.value)

if __name__ == '__main__':
    v = Value('i', 0)
    lock = Lock()
    p10 = [Process(target=func, args=(v, lock)) for x in range(5)]
    for p in p10:
        p.start()
    for p in p10:
        p.join()
        print('parent:',v.value)
    print('value:',v.value)
