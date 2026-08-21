#list   ordered + indexed + mutable/changeable +  written with square brackets[]

# list = [100, 5, True, 3.5, False, "Prashant"]
#
# print(list)
# print(list[:3])
# print(list[1:])
# print(list[:])

# # Example1: How to create list?
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple", 10,"banana",20]
# mylist=list()
#
# print(mylist1, mylist2, mylist3, mylist)


# #Example2: Accessing elements from list
#
# mylist=["apple", "banana", "cherry", 1, False, 100.5, True]
# print(mylist)
#
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
#
#Example3: Range of indexes
# print(mylist[:5])
# print(mylist[2:])
#
# print(mylist[::-1])
#
# print(mylist[-2])
#
# print(mylist[2:5])
#
# print(mylist[0:7])
#
# print(mylist[-7:-1])
#
# mylist_rev = mylist[::-1]
#
# print("Reverse list", mylist_rev)

# #Example4: Change item value
# mylist=["apple", "banana", "cherry"]
# print(mylist)
#
# mylist[1]="orange"
# print(mylist)


# #Example5: Read the list using loop
# mylist=[1, 5, 100]
# print(mylist)
#
# for _ in mylist:
#     print(_)


# #Example6: Check if the item is existing in the list or not
# mylist=["apple", "banana", "cherry"]
#
# if "apple" in mylist:
#     print("Apple is present in the basket")
# else:
#     print("Don't forget to add apple")

# #Example7: List length (counting number of items in the list)
# print(len(mylist))
#
# print(max(mylist))



# #Example8: Add items to the list - append() + insert()
#
# mylist=[1,2,3]
# print(mylist)
# mylist.append("Prashant")
# print(mylist)
#
# mylist.insert(1, "Python")
# print("Here is our updated list: ", mylist)

# #Example9: Remove item from the list
#
# #pop()  FUNCTION >> ()
# mylist=["apple", "banana", "cherry"]
# mylist.append("orange")
# print(mylist)
#
# mylist.pop(0)
# print(mylist)
#
# #del    KEYWORD
# del mylist[1]
#
# print(mylist)
#
# #clear()    FUNCTION >> ()
# mylist.clear()
#
# print(mylist)



# #Example10: Copy list
#
# #list()
# mylist=["cheese", "cherry", "pineapple"]
# print(mylist)
#
# mylist2=list(mylist)
# print(mylist2)
#
# cp_list=mylist[::-1]
# print(cp_list)

# #copy()
# mylist1 = ["cheese", "cherry","pineapple"]
# print(mylist1)
#
# mylist2 = mylist1.copy()
# print(mylist2)



# #Example11: combine/join lists
# #using + operator
#
# list1=['a','b','c']
# list2=[1,2,3]
#
# list3=list2+list1
#
# print(list3)

# #using loop statement
# list1=['a','b','c']
# list2=[1,2,3]
# list3=[]
#
# for i in list1:
#     list3.append(i)
# for j in list2:
#     list3.append(j)
#
# print(list3)

# #extend()
#
# list1=["cheese", "cherry","pineapple"]
# list2=[1,2,3]
#
# list1.extend(list2)
# print(list1)


# l1=[1,2,3]
# l2=[4,5,6,7]
#
# # print(l1+l2)
#
# l1.extend(l2)
# print(l1)


#Example12: Compare lists

list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1.copy()

if list1==list3:
    print("Same lists!")
else:
    print("Different lists!")


