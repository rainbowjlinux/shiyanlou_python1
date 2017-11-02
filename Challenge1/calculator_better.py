#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: calculator_better.py
#Created Time: 2017-10-31 18:14:23
#Author: rainbowjlinux
############################

from collections import namedtuple
import sys

Income_Tax_Calc_Item = namedtuple(
        'Income_Tax_Calc_Item',
        ['Base', 'Rate', 'Subtractor']
        )

INCOME_TAX_TABLE = [
        Income_Tax_Calc_Item(80000, 0.45, 13505),
        Income_Tax_Calc_Item(55000, 0.35, 5505),
        Income_Tax_Calc_Item(35000, 0.3, 2755),
        Income_Tax_Calc_Item(9000, 0.25, 1005),
        Income_Tax_Calc_Item(4500, 0.2, 555),
        Income_Tax_Calc_Item(1500, 0.1, 105),
        Income_Tax_Calc_Item(0, 0.03, 0)
        ]

START_INCOME = 3500

def cal_tax(income):
    if income >= START_INCOME:
        taxable_income = income - START_INCOME
    else:
        return 0.00
    for item in INCOME_TAX_TABLE:
        if taxable_income >= item.Base:
            return taxable_income * item.Rate - item.Subtractor
        else:
            continue

def main():
    if len(sys.argv) != 2:
        print('Parameter Error')
        return
    try:
        income = int(sys.argv[1])
    except ValueError:
        print('Parameter Error')
        return
    
    print(format(cal_tax(income), '.2f'))

if __name__ == '__main__':
    main()
