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

INSURANCE_RATE_TABLE = {
        'indownment' : 0.08,
        'medical' : 0.02,
        'unemployment' : 0.005,
        'injury' : 0.00,
        'maternity' : 0,
        'accumulationfund' : 0.06
        }


START_INCOME = 3500

def cal_tax(income):
    sub_income = income - income * sum(INSURANCE_RATE_TABLE.values())
    taxable_income = sub_income - START_INCOME
    if taxable_income <= 0:
        return sub_income
    for item in INCOME_TAX_TABLE:
        if taxable_income >= item.Base:
            tax = taxable_income * item.Rate - item.Subtractor
            return sub_income - tax

def main():
    if len(sys.argv) < 2:
        print('Parameter Error')
        return
    employee_dic = sys.argv[1:]
    for empl in employee_dic:
        empl_no, empl_income = empl.split(':')
        try:
            income = int(empl_income)
        except ValueError:
            print('Parameter Error')
            return
        tax = cal_tax(income)
        print('{}:{:.2f}'.format(empl_no, tax))
    
if __name__ == '__main__':
    main()
