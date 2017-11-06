#!/usr/bin/env python3

############################
#File Name: multip.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 20:42:28
############################

import os
from multiprocessing import Process, Queue

q = Queue(maxsize=10)

def child1(name):
    print('process:', name, 'pid:', os.getpid())
    q.put('Nice to meet you!')

def child2(name):
    print('process:', name, 'pid:', os.getpid())
    print(q.get())

class Child(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print('class process:', self.name, 'pid:', os.getpid())

if __name__ == '__main__':
    p1 = Process(target=child1, args=('sender', ))
    p2 = Process(target=child2, args=('receiver', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('process: parent', 'pid:', os.getpid())

    child = Child('Use class as process:')
    #child.start()
    child.run()
