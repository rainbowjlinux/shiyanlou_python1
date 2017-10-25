#!/usr/bin/env python3

############################
#File Name: multip.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 20:42:28
############################

import os
from multiprocessing import Process, Pipe

pip1, pip2 = Pipe()

def child1(name):
    print('process:', name, 'pid:', os.getpid())
    pip1.send('Nice to meet you!')

def child2(name):
    print('process:', name, 'pid:', os.getpid())
    print(pip2.recv())

if __name__ == '__main__':
    p1 = Process(target=child1, args=('sender', ))
    p2 = Process(target=child2, args=('receiver', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('process: parent')
    print('pid:', os.getpid())
