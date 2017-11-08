#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: cfgparser.py
#Created Time: 2017-11-08 10:42:44
#Author: rainbowjlinux
############################

import configparser

def main():
    config = configparser.ConfigParser()
    config.read('test.cfg')
    print(type(config.sections()))
    print(type(config['BEIJING']))
    print(config['DEFAULT']['YangLao'])
    pass

if __name__ == '__main__':
    main()
