#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: poly.py
#Created Time: 2017-11-03 15:38:16
#Author: rainbowjlinux
############################

class Person(object):
    def __init__(self, name):
        self.name = name
    def whoami(self):
        print(self.name,"is a person")

class Student(Person):
    def __init__(self, name):
        self.name = name
    def whoami(self):
        print(self.name,"is a student")

class Teacher(Person):
    def __init__(self, name):
        self.name = name
    def whoami(self):
        print(self.name,"is a teacher")

Jimmy = Person('Jimmy')
Jimmy.whoami()
Jack = Student('Jack')
Jack.whoami()
David = Teacher('David')
David.whoami()
