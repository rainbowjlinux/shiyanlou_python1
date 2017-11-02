#!/usr/bin/env python3
import sys

def calculator():
    salary=[1500, 4500, 9000, 35000, 55000, 80000]

    taxrate=[0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

    desal=[0, 105, 555, 1005, 2755, 5505, 13505]

    try:
        if len(sys.argv) != 2:
            raise ValueError
        r = int(sys.argv[1])
        print ("Your salary is {}".format(sys.argv[1], ".2f"))
    except:
        print ("Parameter Error")
        return
    else:
        if (r < 3500):
            print ("You need to pay 0.00")
        else:
            x = r - 3500
            for i in range(6):
                if (x-salary[i] <= 0):
                    y = taxrate[i]
                    z = desal[i]
                    print ("You need to pay {}".format(x * y - z, ".2f"))
                    return
            y = taxrate[i+1]
            z = desal[i+1]
            print ("You need to pay {}".format(x * y - z, ".2f"))
    finally:
        print ("\nThks.")

def main():
    calculator()
    print ("This is a salary tax calculator by wjl\nUsage: ./calculator.py $[INT]")

if __name__ == '__main__':
    main()
