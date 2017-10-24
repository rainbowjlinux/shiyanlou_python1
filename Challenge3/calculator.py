#!/usr/bin/env python3
import sys
import json

def cal_insurance(salary, ins_rate):
    if salary < ins_rate[0]:
        salary = ins_rate[0]
    if salary > ins_rate[1]:
        salary = ins_rate[1]
    return salary * sum(ins_rate[2:])

def cal_tax(income, insurance):
    salary=[1500, 4500, 9000, 35000, 55000, 80000]

    taxrate=[0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

    desal=[0, 105, 555, 1005, 2755, 5505, 13505]

    if (income <= 3500):
        return 0.00
    else:
        x = income - 3500 - insurance
        for i in range(6):
            if (x-salary[i] <= 0):
                y = taxrate[i]
                z = desal[i]
                return x * y - z
        y = taxrate[i+1]
        z = desal[i+1]
        return x * y - z

def load_file(path):
    list = []
    with open (path, 'r') as f:
        for x in f.readlines():
            list.append(x.strip())
        return list

def main():
    try:
        if len(sys.argv) != 7:
            raise ValueError
        cfg_path = sys.argv[2]
        user_path = sys.argv[4]
        gongzi_path = sys.argv[6]
        ins_data = load_file(cfg_path)
        user_data = load_file(user_path)
        employee_id = []
        income = []
        ins_rate = []
        ins = []
        tax = []
        gongzi = []
        outlist = ''
        for x in user_data:
            income.append(int(x.split(',')[1]))
            employee_id.append(x.split(',')[0])
        for x in ins_data:
            ins_rate.append(float(x.split(' = ')[1]))
        for x in income:
            y = cal_insurance(x, ins_rate)
            t = cal_tax(x, y)
            tax.append(format(t, ".2f"))
            ins.append(format(y, ".2f"))
            gongzi.append(format(x - y -t, ".2f"))
        for i in range(3):
            outlist = outlist + employee_id[i] + ',' + str(income[i]) + ',' + ins[i] + ',' + tax[i] + ',' + gongzi[i] + '\n'
        print(outlist)
        with open(gongzi_path,'w') as f:
            f.writelines(outlist)
    except:
        print ("Parameter Error")
        return
    finally:
        print ("\nThks.")
        print ("This is a salary tax calculator by wjl\nUsage: ./calculator.py -c test.cfg -d user.csv -o gongzi.csv]")

if __name__ == '__main__':
    main()
