# # 1
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mco1 = MyClass()
# mco2 = MyClass()
#
# res = mco1.myfun()
# print(res)
#
# mco1.display("Prashant")
# mco2.display("Pansare")
from setuptools.namespaces import flatten

# # 2
# class MyClass:
#     def m1(self):
#         print("Instance method...")
#
#     @staticmethod
#     def m2():
#         print("Static method...")
#
#     @staticmethod
#     def m3(name):
#         print(name)
#
# mco1 = MyClass()
# mco1.m1()
# MyClass().m1()
# MyClass.m2()
# MyClass.m3("Prashant")

# # 3
# class MyClass:
#     a,b = 10,20
#     def add(self):
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a * self.b)
#
# mco = MyClass()
# mco.add()
# mco.mul()


# #4
# i,j = 15,25                         # Global variables
# class MyClass:
#     a,b = 10,20                     # Class variables
#     def add(self,x,y):              # Local variables
#         print(x+y)
#         print(self.a + self.b)
#         print(i+j)
#
# mco = MyClass()
# mco.add(50,100)

# #5
# a,b = 10,20
# class MyClass:
#     a,b = 100,200
#     def add(self):
#         a,b = 1000,2000
#         print(a+b)
#         print(self.a + self.b)
#         print(globals()['a']+globals()['b'])
#
# mco = MyClass()
# mco.add()


# # 6
# class MyClass:
#     def display(self,name):
#         print(name)
#
# mco1 = MyClass()
# mco1.display("Prashant")
#
# mco2 = MyClass()
# mco2.display("Pansare")


# # 7: Constructor
# class MyClass:
#     def __init__(self):
#         print("This is constructor...")
#
#     def m1(self):
#         print("Hello...")
#
#     def m2(self,x,y):
#         return x+y
#
# mco = MyClass()
# mco.m1()
# res = mco.m2(10,20)
# print(res)


# # 8
# class MyClass:
#     name = "John"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# mco = MyClass("Scott")

# 9
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        return self.ename

    def display(self):
        print(f"Employee with id {self.eid} named {self.ename} has secured salary {self.esal} LPA.")

empo = Emp(1000,"Prashant",30.50)
print(empo)
empo.display()