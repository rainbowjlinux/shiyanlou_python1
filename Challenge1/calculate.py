#!/usr/bin/env python3
import sys

#print (sys.argv)

def salcal():
    salary=[1500, 4500, 9000, 35000, 55000, 80000]
    
    taxrate=[0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
    
    desal=[0, 105, 555, 1005, 2755, 5505, 13505]
    
    r = int(sys.argv[1])
    
    if (r < 3500):
        print ("%.2f" % 0)
    else:
        x = r - 3500
        for i in range(6):
            #print (i)
            if (x-salary[i] <= 0):
                y = taxrate[i]
                z = desal[i]
                #print(x, y, z)
                print ("%.2f" % (x * y - z))
                return
        y = taxrate[i+1]
        z = desal[i+1]
        #print(x, y, z)
        print ("%.2f" % (x * y - z))

def main():
    salcal()

if __name__ == '__main__':
    main()
