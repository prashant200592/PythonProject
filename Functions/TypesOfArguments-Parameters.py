
#Arguments/Parameters >> a. Positional arguments b. Keyword arguments

# #Example1:
#
# def fun(a,b):
#    print(a,b)
#
# fun(10,20)      #Positional arguments
# fun(b=10,a=20) #Keyword arguments


# #Example2:  Default value assigned to the positional argument
#
# def fun(i=5, j=10):
#     print(i,j)
#
# fun(100,200)    #100 200
# fun(100)        #100 10
# fun()           #5 10


# #Example3: Keyword arguments
#
# def fun(name, greetmsg):
#     print(greetmsg+" "+name)
#
# fun(name="Prashant", greetmsg='Hello')
# fun(greetmsg="Hello", name="Prashant")


# #Example4: Positional and Keyword Arguments
#
# def fun(a,b,c):
#     print(a,b,c)
#
# fun(10,20,30)                   #Positional arguments
# fun(b=20, c=30, a=10                           )           #Keyword arguments
# fun(10, b=20, c='Prashant')     #Positional AND Keyword arguments
# #fun(a=30, 10,20)                #positional argument follows keyword argument: It should come first
# fun(10,20,c=30)



#Example5: Return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(100,200))     #(200, 100)
print(largest(20,10))       #(20, 10)

res = largest(100,200)
print(res)
print(type(res))            #<class 'tuple'>

