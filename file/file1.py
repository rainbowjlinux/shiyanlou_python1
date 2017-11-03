#!/usr/bin/env python3

############################
#File Name: file1.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-23 10:55:17
############################

from collections import Iterable

def openfile(path):
    print ('file path:',path)
    f = open(path)
    print ('===read once===')
    l = f.read()
    f.close()

    f = open(path)
    print ('===read twice===')
    l = f.readlines()
    for x in l:
        print(x)
    f.close()

def openwith(path):
    print('use \'with\' can avoid to forget close file')
    with open(path) as f:
        print (f.read())

def writefile(path):
    with open(path, 'a') as f:
        f.write('python lesson6\n')
    with open(path, 'r') as f:
        print(f.read())

def copyfile(src, dst):
    with open(src, 'r') as s:
        print('===read from test===')
        tmp = s.read()
    with open(dst, 'w') as d:
        print('===write to copy===')
        d.write(tmp)
    with open(dst, 'r') as d:
        print('===read copy===')
        print(d.read())

def copywith(src, dst):
    with open(src, 'r') as s:
        with open(dst, 'w') as d:
            d.write(s.read())

def readfile(filepath):
    with open(filepath, 'r') as f:
        for line in f.read():
            print(line)

def traverse(filepath):
    with open(filepath, 'r') as f:
        print("f is iterable?", isinstance(f, Iterable))
        for line in f:
            print(line)

def main():
    file1 = "/home/shiyanlou/Code/shiyanlou_python1/file/test.txt"
    file2 = "/home/shiyanlou/Code/shiyanlou_python1/file/copy.txt"
    openfile(file1)
    openwith(file1)
    writefile(file1)
    copyfile(file1, file2)
    copywith(file1, file2)
    print('===copy successfully===')
    traverse(file1)

if __name__ == '__main__':
    main()
