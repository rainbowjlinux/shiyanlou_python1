#!/usr/bin/env python3

############################
#File Name: mod.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-26 20:37:30
############################

from datetime import datetime, date, timedelta
import os, sys
import requests
from collections import namedtuple

if __name__ == '__main__':
    print(date.today())
    t = datetime.now()
    print(datetime.strftime(t, '%Y-%m-%d'))
    print(t.strftime('%H:%M'))
    print(t.year)
    print(t.month)
    print(t.day)
    print(t.hour)
    print(t.minute)
    print(t.second)
    delta = timedelta(weeks=1, days=1, hours=1, minutes=1)
    print(delta)
    print(t+delta)

    print(os.getcwd())
#    os.mkdir('web')
#    os.mknod(os.getcwd()+'/new.py')
    print(os.urandom(1))
    print(sys.argv)

    r = requests.get('https://www.baidu.com')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.headers['date'])

    q = requests.get('https://api.github.com')
    print(type(q.json()))
    print(q.json())

    P = namedtuple('Point', ['x','y'])
    p = P(1,2)
    print(p.x, p.y)
