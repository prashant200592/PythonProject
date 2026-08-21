
#Example10: Overloading >> Polymorphism

# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello "+name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayhello()
# h.sayhello("Prashant")



#Example11: Overloading 2 >> Polymorphism

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

cal=Calculation()
cal.add()
cal.add(10,20)
cal.add(100,200,300)



