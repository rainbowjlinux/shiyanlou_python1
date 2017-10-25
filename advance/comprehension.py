#!/usr/bin/env python3

############################
#File Name: comprehension.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 14:48:36
############################

if __name__ == '__main__':

    #list comprehension
    even1 = [x for x in range(10) if x%2 == 0]
    print('use comprehension:')
    print (even1)

    print('use filter:')
    print(list(filter(lambda x: x%2 == 0, range(10))))

    even2 = [x*x for x in range(10)]
    print('use list comrehension to cal square:')
    print(even2)

    #@filter usage
    print('use filter to grep words:')
    def is_not_empty(s):
        return s and len(s.strip()) > 0
    empty1 = filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
    print(list(empty1))

    empty2 = filter(lambda x: x and len(x.strip()), ['hello', '', 'world', None])
    print(list(empty2))

    #dict comprehension
    print('use dict comprehension:')
    income = {'zhangsan':1000, 'zhaosi':2000, 'liuneng':3000}
    tax = {key:value*0.2 for key,value in income.items()}
    print(tax)
