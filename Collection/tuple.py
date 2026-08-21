#tuple
#multiple values + ordered + indexed + immutable + written with () + more secure than list[]  + fast

# #Example1: Create tuple
#
# mytuple=("cheese", "cherry", "pineapple")
# mytuple1=tuple()
#
#print(mytuple1)

# #Example2: Access tuple items
#
# mytuple=("cheese", "cherry", "pineapple")
# print(mytuple[1])
# print(mytuple[-1])


# #Example3: Range of tuple indexes
# mytuple=("cheese", "cherry", "pineapple", 1,2,3,True, 'a','b')
# print(mytuple)
# print(mytuple[2:5])
# print(mytuple[-8:-1])


# #Example4: Changing tuple value >> workaround: tuple > list > tuple
#
# mytuple=("cheese", "cherry", "pineapple")
# mylist=list(mytuple)
#
# mylist[0]="berry"
#
# mytuple=tuple(mylist)
#
# print(mytuple)


# #Example5: Reading tuple items
# #loop
#
# mytuple=("cheese", "cherry", "pineapple", 1,2,3,True, 'a','b')
#
# for i in mytuple:
#     print(i)



# #Example6: Search item in tuple
#
# mytuple=("cheese", "cherry", "pineapple", 1,2,3,True, 'a','b')
#
# if "cheese" in mytuple:
#     print("We got cheese!")
# else:
#     print("Don't forget to add cheese!")



# #Example7: Tuple length - Counting items in tuple
#
# mytuple=("cheese", "cherry", "pineapple", 1,2,3,True, 'a','b')
#
# print(len(mytuple))
#
# #print(max(mytuple)) #need same data type
# #print(min(mytuple)) #need same data type


# #Example8: Add items in tuple - Not possible - Workaround: tuple > list > tuple
#
# mytuple=("cheese", "cherry", "pineapple", 1,2,3,True, 'a','b')
#
# #mytuple[0]="c" #Not possible
#
# mylist = list(mytuple)
# mylist.append("Prashant")
# mylist.insert(1, "False")
# mytuple=tuple(mylist)
#
# print(mytuple)


# #Example9: copy tuple
# mytuple = ('cheese', 'False', 'cherry', 'pineapple', 1, 2, 3, True, 'a', 'b', "Prashant")
#
# mytuple2=mytuple
#
# print(mytuple2)


# #Example 10: Remove items from tuple
# mytuple = ('cheese', 'False', 'cherry', 'pineapple', 1, 2, 3, True, 'a', 'b', "Prashant")
#
# #mytuple.pop(0)
#
# #del mytuple #Deleted tuple
#
# #mytuple.clear()
#
# print(mytuple)


# #Example11: join/combine tuple
# + operator
# mytuple1 = ('cheese', 'False', 'cherry')
# mytuple2 = (1,2,3)
# mytuple3 = mytuple1+mytuple2
# print(mytuple3)

# for loop
# mytuple1 = ('cheese', 'False', 'cherry')
# mytuple2 = (1,2,3)
# mylist = []
# print(mylist)
# for i in mytuple1:
#     mylist.append(i)
#
# for j in mytuple2:
#     mylist.append(j)
#
# mytuple3=tuple(mylist)
#
# print(mytuple3)



#Example12: compare tuples
tuple1=(10,20,30)
tuple2=('a','b','c')
tuple3=tuple1

if tuple1==tuple3:
    print("Same tuples")
else:
    print("Different tuples")

