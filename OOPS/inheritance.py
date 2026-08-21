#Inheritance
# Objectives: 1. Code re-usability 2. Avoid duplication
# Types:
    # 1. Single (one parent - one child)
    # 2. Multi level (one parent - child > child > child) - last generation will contain everything from all ancestors
    # 3. Heirarchy (one parent - any number of childs) - different child classes
    # 4. Multiple (multiple parents - single child)

#Example1:      Single inheritance
# class A:
#     def m1(self):
#         print("This is m1 method from Class A")
#
# class B(A):
#     def m2(self):
#         print("This is m2 method from Class B")
#
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# aobj = A()
# aobj.m1()

#Example2:      Single inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B (A):
#     a,b=200,100
#     def m2(self):
#         print(self.a - self.b)
#
# a=A()
# a.m1()
#
# b=B()
# b.m2()
# b.m1()

#Example3: Multi level inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# c = C()
# c.m1()
# c.m2()
# c.m3()



#Example4: Heirarchy inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     i,j=200,100
#     def m2(self):
#         print(self.i-self.j)
#
# class C(A):
#     a,b=5,2
#     def m3(self):
#         print(self.a*self.b)
#
# b=B()
# b.m1()
# b.m2()
#
# c=C()
# c.m1()
# c.m3()



#Example5: Multiple inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# c=C()
# c.m1()
# c.m2()
# c.m3()



#Example6: Same method in child class (Over-riding) #Calling parent class using child class >> super()

# class A:
#     def m1(self):
#         print("This is m1 from Class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 from Class B")
#         super().m1()
#
#
# b=B()
# b.m1()


#Example7:  Access parent class variables

# class A:
#     a,b=20,10
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)              #local variables
#
#         print(self.i+self.j)    #class variables
#
#         print(self.a+self.b)    #class variables
#
#
# b=B()
# b.m(1000,2000)



#Example8: Overriding variables

# class Parent:
#     name="Prashant"
#
# class Child(Parent):
#     name="PrashPython"
#
#     def test(self):
#         print(super().name)
#
# c=Child()
# print(c.name)
# c.test()



#Example9: Overriding methods

# class Bank:
#     def rateOfInterest(self):
#         return 0
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
# x=XBank()
# print(x.rateOfInterest())
#
# y=YBank()
# print(y.rateOfInterest())


#Example10: Overloading >> Polymorphism

class Cal():
    def add(self,a=0,b=0,c=0,d=0,e=0):
        print(a+b+c+d+e)
obj = Cal()
obj.add()
obj.add(1)
obj.add(1,2)
obj.add(1,2,3)
obj.add(1,2,3,4)
obj.add(1,2,3,4,5)
# obj.add(1,2,3,4,5,6)  # TypeError: Cal.add() takes from 1 to 6 positional arguments but 7 were given











