#set
#multiple values + unordered + unindexed + written by {}

# #Example1: Create set
#
# myset = {"Cheese", 10.5, 'a', True, "Prashant", 5, False}
# print(myset)

# #Example2: Accessing set items
#
# myset = {"Cheese", 10.5, 'a', True, "Prashant", 5, False}
#
# for i in myset:
#     print(i)


# #Example3: Check if value present in set or not
# myset = {"Cheese", 10.5, 'a', True, "Prashant", 5, False}
#
# if "Cheese" in myset:
#     print("Cheese present!")
# else:
#     print("Don't forget to buy a Cheese!!!")
#
#
# print('a' in myset)
# print(10.500000 in myset)


# #Example4: adding items to set
# #add() - add single item
# #update() - add multiple items
#
# myset = {"Cheese", 10.5, 'a', True, "Prashant", 5, False}
#
# myset.add("orange")
#
# print(myset)
#
# myset.update("l", "m", 'Python')
# print(myset)


# #Example5: find number of items in set
#
# myset = {False, True, 'P', 5, 'm', 'n', 'l', 10.5, 'Prashant', 't', 'o', 'orange', 'a', 'Cheese', 'h', 'y'}
#
# print(len(myset))


# #Example6: Remove item/s to set
#remove()
#discard()

# myset = {False, True, 'P', 5, 'm', 'n', 'l', 10.5, 'Prashant', 't', 'o', 'orange', 'a', 'Cheese', 'h', 'y'}
# myset.remove("orange")
# print(myset)


# myset = {False, True, 'P', 5, 'm', 'n', 'l', 10.5, 'Prashant', 't', 'o', 'orange', 'a', 'Cheese', 'h', 'y'}
# myset.discard("orange1")        #No error when incorrect key is used
# print(myset)



# #Example7: Clear all the items from set
# #clear() - Function
# #del - Keyword
#
# myset = {False, True, 'P', 5, 'm', 'n', 'l', 10.5, 'Prashant', 't', 'o', 'orange', 'a', 'Cheese', 'h', 'y'}
#
# myset.clear()
#
# print(myset)
#
# del myset
#
# print(myset)


# #Example8: join 2 sets
# #union()
#
# set1 = {"a", "b", "c", 1}
# set2 = {1,2,3}
#
# set3=set1.union(set2)
# ##set3=set1.intersection(set2)
#
# print(set3)

# set1 = {"a", "b", "c", 1}
# set2 = {1,2,3}
# #set3 = {}
# #set3 = set1.update(set2)
#
# set1.update(set2)
#
# print(set1)

###Testing new approach
# set1 = {"a", "b", "c", 1}
# set2 = {1,2,3}
# set3 = {}
#
# for i in set1:
#     set3.add(i)
# for j in set2:
#     set3.add(j)
#
# print(set3)