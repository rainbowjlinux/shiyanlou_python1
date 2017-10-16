#!/usr/bin/env python3

try:
    f = open("/home/shiyanlou/Code/shiyanlou_python1/exception/readonly.py")
    f.write("shiyanlou")
except FileNotFoundError:
    print("File not found")
except:
    print("write fail")
finally:
    print("finally")
    f.close()
