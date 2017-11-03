#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: person.py
#Created Time: 2017-11-03 13:59:56
#Author: rainbowjlinux
############################

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)
        print(age)

class Student(Person):
    def __init__(self, name, age, score):
        super(Student, self).__init__(name, age)
        self.score = score
        print(score)

class Teacher(Person):
    def __init__(self, name, age, course):
        super(Teacher, self).__init__(name, age)
        self.course = course
        print(course)

Jack = Person('Jack', 18)
Jimmy = Student('Jimmy', 20, 100)
David = Teacher('David', 30, 'English')

print(Jimmy.score)
print(David.course)

print(isinstance(Jack, Student))
print(isinstance(Jimmy, Person))
print(isinstance(Jimmy, Teacher))
print(isinstance(Jimmy, object))
print(isinstance(David, Teacher))
