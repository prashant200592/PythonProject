

# #Example1:
#
# global_var=20       #Global variable
#
# def fun():
#     local_var=10    #Local variable
#     print(local_var)
#     print(global_var)
#
# fun()
#
# print(global_var)
# #print(local_var)       #Not accessible


# #Example2:
# xy = 100
#
# def cool():
#     xy=200
#     print(xy)
#
# cool()
# print(xy)


# #Example3:
#
# xy = 100
#
# def cool():
#     global xy
#     xy = 200        #Global variable now
#     print(xy)
#
# cool()


# #Example4:
#
# x = 100
#
# def cool():
#     global x
#     x = 500
#     print(x)
#
# print(x)    #100
# cool()      #500
# print(x)    #500


#Example5:  Global variable inside the function

def cool():
    global x
    x = 100
    print(x)

#print(x)   #Invalid >> Cannot access it - name 'x' is not defined
cool()      #100
print(x)    #100    Valid >> Can access it outside the function

