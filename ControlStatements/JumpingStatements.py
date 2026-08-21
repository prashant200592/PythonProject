#Jumping statements
#Break
#Continue

for i in range(1,11):
    if i==5:
        break
    print(i)        #1..9

print("Programme exited!!!")

for i in range(1,11):
    if i==5 or i==3 or i==7:
        continue
    print(i)

print("Program exited!!!")

print("Max number is: ", max(100, 1, 50, 150, 3, 100, 3, 50, 500.5))

print("Minimum number is: ", min(-100, 50.5, 150, -505.5005))


