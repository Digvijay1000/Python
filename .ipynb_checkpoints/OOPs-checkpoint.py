"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)"""

# ---------------------------------------------------------------------------------------------------------------------
"""class student:

    rollno =12
    name = 'Yuvi'
    branch = 'BCCI'

    def read(self):
        print('Reading......')

    def write(self):
        print('writing......')

# object name = class_name ()

s = student()
s1 = student()
s3 = student()

s.read()
s1.read()
s3.write()
student.read()"""

# ------------------------------------------------------------------------------------------------------------------

"""class student():
    roll_no = 27 # global/instance variable
    print('global variable from outside the function',roll_no)
    def read(self):
        roll_no = 10 # local variable
        print('local variable "roll_no" :',roll_no)
        print('global variable from function :',self.roll_no)

obj1 = student()
obj1.read()
"""
# -------------------------------------------------------------------------------------------------------------
# with inheritance
# class parent: # BASE CLASS
#     def display(self):
#         print('PARENT')
#
# class child(parent): # DERIVED CLASS
#     def show(self):
#         print('CHILD')
#
# c1 = child()
# c1.show()
# c1.display()
#
# # without inheritance
# class parent: # BASE CLASS
#     def display(self):
#         print('PARENT')
#
# class child: # DERIVED CLASS
#     def show(self):
#         print('CHILD')
#
# c1 = child()
# p1 = parent()
# c1.show()
# p1.display()

#
# class Grandparaent: # BASE CLASS
#     def gdisplay(self):
#         print("GRAND PARAENT")
#
# class paraent(Grandparaent): # DERIVED CLASS
#     def pdisplay(self):
#         print("PARAENT ")    # BASE CLASS
#
# class child(paraent): # DERIVED CLASS
#     def cdisplay(self):
#         print("CHILD")
#
# g1 = child()
# g1.gdisplay()
# g1.pdisplay()
#

# class Animal:
#     def speak1(self):
#         pass
#
# class Dog(Animal):
#     def speak2(self):
#         return "bho! bho!"
#
# class Cat(Animal):
#     def speak3(self):
#         return "Meow! Meow!"
#
# dog = Dog()
# cat = Cat()
#
# print('moti says',dog.speak2()) # bho bho
# print('mani says',cat.speak3()) # mau mau

# class father: # base class 1
#     def fdisplay(self):
#         print('FATHER')
#
# class mother: # base class 2
#     def mdisplay(self):
#         print('MOTHER')
#
# class son(father, mother):
#     def sdisplay(self):
#         print('SON')
#
# obj = son()
# obj.fdisplay()
# obj.mdisplay()
# obj.sdisplay()

# class father:
#     def fdisplay(self):
#         print("FATHER")
#
# class son1(father):
#     def s1display(self):
#         print("SON 1")
#
# class son2(father):
#     def s2display(self):
#         print("SON 2")
#
# s1 = son1()
# s2 = son2()
# s1.s1display()
# s2.s2display()
# s1.fdisplay()
# s2.fdisplay()

# class encap:
#     a = 10
#     def display(self):
#         print("WEL-COME")
#
# obj = encap()
# print(obj.a)
# obj.display()

# class encap:
#     __a = 10
#     def __display(self):
#         print("WEL-COME")
#         print(self.__a)
#
# obj = encap()
# print(obj.a)
# obj.display()

# --------------------------------------------------------------------------------------------------------------------
# from abc import ABC, abstractmethod
#
# class AbstractDemo(ABC):    # Abstarct Class
#     @ abstractmethod        # Decorater
#     def display(self):
#         print('we are in the AbstarctClass')
#
# class Demo(AbstractDemo):   # Concreate Class
#     def display(self):
#         print('ABSTARCT METHOD')
#
# obj = Demo()
# obj.display()

# ----------------------------------------------------------------------------------------------------------------

# Polymorphism : implementing the same thing in different way
# 1. concatinating
# a = "Hello "
# b = "Wel Come"
# c = a + b
# print(c)

# 2. addition
# a = 100
# b = 300
# c = a + b
# print(c)

#
# class moverload:
#     def display(self,a=None,b=None):
#         print(a,b)
#
# obj = moverload()
# obj.display()
# obj.display(100,)
# obj.display(1000,1000)

# class father:
#     def transport(self):
#         print('CYCLE')
#
# class son(father):
#     def transport(self):
#         print('BIKE')
#
# obj=son()
# obj.transport()
