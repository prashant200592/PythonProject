
#Example1:

# #a
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self):
#         print("Prashant")
#
# mc1=MyClass()
# mc1.myfun()
# mc1.display()
#
# MyClass().display()

# #b
#
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# MyClass().display("Prashant")


# #Example2:
#
# class MyClass:
#     def m1(self):
#         print("This is instance/object method")
#
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# mc = MyClass()
# mc.m1()
# MyClass.m2(10,100)


# #Example3:  Class variables
#
# c = 100
#
# class MyClass:
#
#     a, b = 10, 20       #Class variables
#
#     def add(self):
#         print(self.a + self.b)
#
#     def mul(self):
#         print(self.a*self.b)
#
# mc = MyClass()
# mc.add()
# mc.mul()


# #Example4: Global+Class+Local Variables
#
# i,j=15,25
#
# class MyClass:
#     a,b=10,20
#
#     def add(self,x,y):
#         print(x+y)
#
#         print(self.a+self.b)
#
#         print(i+j)
#
# mc = MyClass()
# mc.add(100,200)



# #Exaple5: Global+Class+Local Variables >> Same variables at all 3 places
#
# a,b = 15,25
#
# class MyClass:
#     a,b = 10,20
#
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
#
# mc = MyClass()
# mc.add(100,200)


# #Example6: One class can have multiple objects
#
# class MyClass:
#     def display(self,name):
#         print("This is display method...")
#         print(name)
#
# obj1 = MyClass()
# obj1.display("Prashant")
#
# obj2 = MyClass()
# obj2.display("Python")



# #Example7: Constructor
#
# class MyClass:
#
#     def __init__(self):
#         print("This is constructor...")
#
#     def m1(self):
#         print("Hello Prashant!!!")
#
#     def add(self,a,b):
#         print(a+b)
#
# obj = MyClass()     #Invokes constructor automatically
# obj.m1()            #Method called explicitely using an object
# obj.add(10,20)      #30



# #Example8: Constructor with an argument
#
# class MyClass:
#     name='Prashant'
#     def __init__(self,name):        #Constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=MyClass("Python")        #Passing parameter to the constructor



# Example9: One constructor + One method to print employee details
# Req: Emp
#     constructor: eid, ename, sal
#     display(): print eid, ename and sal

# class Emp:
#     def __init__(self,eid,ename,sal):
#         print(eid)
#         print(ename)
#         print(sal)
#
#     def display(self, eid, ename, sal):
#         print(eid)
#         print(ename)
#         print(sal)
#
# obj = Emp(20389,"Prashant", 110000)        #Invoke constructor
#
# obj.display(1,"Prash",150000)                  #Invoke method display()


# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(20389, "Prashant", 150000)
# e1.display()
#
# e2=Emp(1,"Anand",1000000)
# e2.display()


# #Example10: 2 Constructors
# class Emp:
#
#     def __init__(self,eid, ename, sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def __str__(self):
#         return(self.ename)      #__str__(self) only returns String data
#
#
# e1 = Emp(1, "Prashant", 150000)
#
# e2 = Emp(2, "Rajesh", 200000)
#
# print(e1)
# print(e2)





