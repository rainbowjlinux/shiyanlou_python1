#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: poly.py
#Created Time: 2017-11-03 14:51:04
#Author: rainbowjlinux
############################

import json

class Student(object):
    def __init__(self, name):
        self.name = name
    def read(self):
        return self.name

def main():
    s = Student('["Jimmy", "Jack"]')
    print(json.load(s))
    
if __name__ == '__main__':
    main()
