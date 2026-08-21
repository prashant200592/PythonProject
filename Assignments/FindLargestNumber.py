num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 > num2 and num2 > num3:
    print("1st number is largest!")
elif num2 > num1 and num1 > num3:
    print("2nd number is largest!")
else:
    print("3rd number is largest!")

#print("Largest number is: ", max(num1, num2, num3))

