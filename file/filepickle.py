#!/usr/bin/env python3

############################
#File Name: file2.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-23 15:34:24
############################

import pickle

def dumpdict(dic, fil):
    with open(fil, 'wb') as f:
        pickle.dump(dic, f)

def loaddict(fil):
    with open(fil, 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    dictname = {'zhangsan':1000,'zhaosi':2000,'liuneng':3000}
    filename = '/home/shiyanlou/Code/shiyanlou_python1/file/dic1.data'
    print('dump dict')
    dumpdict(dictname, filename)
    print('load dict')
    d = loaddict(filename)
    print (d)
