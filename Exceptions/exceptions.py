#Example1:
# print("This is starting point...")
# print("This is starting point...")
# print("This is starting point...")
# try:
#     print(x)
# except:
#     print("Exception occurred")
# print("This is end of the program...")
# print("This is end of the program...")
# print("This is end of the program...")

#Example2:
# print("This is starting point...")
# print("This is in progress...")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception occurred...handled...")
# print("This program completed...")

#Example3: Multiple except blocks: try > except > else > finally
# try:
#     num1, num2 = 10, 5
#     result = num1/num2
#     print("Result is ", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception...")
# except SyntaxError:
#     print("Thrown SyntaxError exception...")
# except:
#     print("Exception handled...")
# else:
#     print("No exceptions occurred...")
# finally:
#     print("Always execute...")

#Example4: Raising our own exception

# def enterage(num):
#     if num < 0:
#         raise ValueError("Only integers are allowed")
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# #enterage(-1)
#
# print("Checking exception...")
# num = -1
# try:
#     enterage(num)
# except:
#     print("ValueError exception occurred and handled...")
# print("Program completed...")


def enterage(num):
    if num%2 == 0:
        print("even")
    elif num < 0:
        raise ValueError("Enter positive number")
    else:
        print("odd")


#enterage(-1)

num = -1
print("Testing program...")
try:
    enterage(num)
except ValueError:
    print("ValueError found and handled...")
else:
    print("No error found...")
finally:
    print("Program completed...")


















