#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: calculator_better.py
#Created Time: 2017-10-31 18:14:23
#Author: rainbowjlinux
############################

from collections import namedtuple
import sys, csv

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

class ArgsSplit(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def _get_option_value(self, option):
        index = self.args.index(option) + 1
        return self.args[index]
    @property
    def _config_path(self):
        return self._get_option_value('-c')
    @property
    def _userdata_path(self):
        return self._get_option_value('-d')
    @property
    def _export_path(self):
        return self._get_option_value('-o')

args = ArgsSplit()

class Config(object):
    def __init__(self, path):
        self.path = path
        self.config = self._read_config()

    def _read_config(self):
        config_dict = {}
        with open(self.path, 'r') as f:
            for item in f.readlines():
                key, val = item.split('=')
                try:
                    config_dict[key.strip()] = float(val.strip())
                except:
                    print("Parameter Error")
                    exit()
        return config_dict

    def _get_config(self, key):
        try:
            return self.config[key]
        except:
            print("Config Error")
            exit()

    @property
    def _insurance_low(self):
        return self._get_config("JiShuL")

    @property
    def _insurance_high(self):
        return self._get_config("JiShuH")

    @property
    def _insurance_rate(self):
        INSURANCE_RATE_TABLE = [
                self._get_config("YangLao"),
                self._get_config("YiLiao"),
                self._get_config("ShiYe"),
                self._get_config("GongShang"),
                self._get_config("ShengYu"),
                self._get_config("GongJiJin")
                ]
        return INSURANCE_RATE_TABLE

config = Config(args._config_path)

class Userdata(object):
    @property
    def _read_userdata(self):
        with open(args._userdata_path, 'r') as f:
            userdata = []
            for line in f.readlines():
                employee_id, income = line.split(',')
                try:
                    income = int(income)
                except ValueError:
                    print("Parameter Error")
                    exit()
                userdata.append([employee_id, income])
        return userdata

userdata = Userdata()

class Calc_income_tax(object):
    @staticmethod
    def _insurance(income):
        if income < config._insurance_low:
            return config._insurance_low * sum(config._insurance_rate)
        if income > config._insurance_high:
            return config._insurance_high * sum(config._insurance_rate)
        return income * sum(config._insurance_rate)

    @classmethod
    def _tax_realincome(cls, income):
        sub_income = income - cls._insurance(income)
        taxable_income = sub_income - START_INCOME
        if taxable_income <= 0:
            return 0.00, sub_income
        for item in INCOME_TAX_TABLE:
            if taxable_income >= item.Base:
                tax = taxable_income * item.Rate - item.Subtractor
                return tax, sub_income - tax

    def export(self):
        for result in userdata._read_userdata:
            tax, realincome = self._tax_realincome(result[1])
            ins = self._insurance(result[1])
            result.append('{:.2f}'.format(ins))
            result.append('{:.2f}'.format(tax))
            result.append('{:.2f}'.format(realincome))
            with open(args._export_path, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(result)

def main():
    if len(sys.argv) != 7:
        print('Parameter Error')
        return
    calculator = Calc_income_tax()
    calculator.export()

if __name__ == '__main__':
    main()
