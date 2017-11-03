#!/usr/bin/env python3

############################
#File Name: json.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-23 15:58:08
############################

import json

def dumpfile(filename,dic):
    with open(filename,'w') as f:
        s = json.dumps(dic)
        print ('dump:',s)
        f.write(s)

def loadfile(filename):
    with open(filename,'r') as f:
        s = f.read()
        print('load:',s)
        return json.loads(s)
def main():
    dic = {'zhangsan':1000,'zhaosi':2000,'liuneng':3000}
    filename = '/home/shiyanlou/Code/shiyanlou_python1/file/dic2.data'
    dumpfile(filename, dic)
    new_dic = loadfile(filename)
    print (type(new_dic))

    with open('/home/shiyanlou/Code/shiyanlou_python1/file/test_iter.txt', 'r') as f:
        print(json.loads(f.read()))
    with open('/home/shiyanlou/Code/shiyanlou_python1/file/test_iter.txt', 'r') as f:
        print(json.load(f))

if __name__ == '__main__':
    main()
