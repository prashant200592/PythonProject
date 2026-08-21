#Conditional Statements
#   if      if..else        elif

#Example1: Print if person is eligible for vote or not
#age >= 18

# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print("Congratulation, you are eligible for voting!!!")
#
# else:
#     print("You can vote after ", 18-age, "years!!!")

#Example2
#if True:

# if False:
#     print("True condition here")
# else:
#     print("False Condition here")

#Example3

# if 1:
#     print("Switched on")
# else:
#     print("Switched off")

#Example4: Find even number

#num = int(input("Enter any number: "))

# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")


#Example5: if else in single line (ternary operator)

# num = int(input("Enter any number: "))
#
# print ("Even number!") if num%2==0 else print("Odd number!")


#Example6: if else multiple statements (ternary operator)

# a=11
#
# {print("Hello"), print("Python")} if a>=10 else {print("Hello"), print("Java")}


#Example7: Multiple conditions using elif

weekno=1

if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tuesday")
elif weekno==4:
    print("Wednesday")
elif weekno==5:
    print("Thursday")
elif weekno==6:
    print("Friday")
elif weekno==7:
    print("Saturday")
else:
    print("Invalid Day")

 

