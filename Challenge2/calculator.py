#!/usr/bin/env python3
import sys

def cal_insurance(salary):
    ins_rate=[0.08, 0.02, 0.005, 0, 0, 0.06]
    return salary * sum(ins_rate)

def cal_tax(income, insurance):
    salary=[1500, 4500, 9000, 35000, 55000, 80000]

    taxrate=[0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

    desal=[0, 105, 555, 1005, 2755, 5505, 13505]

    if (income < 3500):
        print ("You need to pay 0.00")
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

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError
        s = int(sys.argv[1])
        print (s)
    except:
        print ("Parameter Error")
        return
    else:
        r = cal_insurance(s)
        print (r)
        t = cal_tax(s, r)
        print (t)
        q = s - r - t
        print (format(q, ".2f"))
    finally:
        print ("\nThks.")
        print ("This is a salary tax calculator by wjl\nUsage: ./calculator.py $[INT]")

if __name__ == '__main__':
    main()
