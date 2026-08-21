#dictionary
#unordered + mutable + indexed + written with {} + key:value pairs

# #Example1: Creating dictionary
#
# dic = {'A':"Apple", 'P':"Prashant", 101:"x", 102:"y", 103:"z"}
# print (dic)
#
# print(dic.keys())
# print(dic.values())


# #Example2: Accessing items from dictionary
#
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
#
# print(mydic["brand"])
# print(mydic["model"])
#
# #using get()
#
# x = mydic.get("year")
# print(x)
#
# print(mydic.get("model"))


# #Example3: Changing values in Dictionary
#
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# print(mydic)
#
# mydic["year"] = 2023    #new value: 2023
# print(mydic)


# #Example4: Reading items from Dictionary
#
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2023
# }
# print(mydic)
#
# for i in mydic:
#     print(i)        #prints only keys from dictionary
#
#
# for i in mydic:
#     print(mydic[i])     #print only values from dictionary
#
# for i in mydic.values():
#     print(i)            #print only values from dictionary
#
# for x,y in mydic.items():
#     print(x,y)          #print keys:values
#
# for i in mydic:
#     print(i, mydic[i])  #print keys:values


# #Example5: Check key in dictionary
#
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
# print(mydic)
#
# if "brand" in mydic:
#     print("Brand data is available!")
# else:
#     print("Don't forget to add brand information")
#
# print("model" in mydic)     #True

# #Example6: Total number of items in dictionary
#
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
#
# print(len(mydic))


# #Example7: Adding items to the Dictionary
#
# mydic = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2021
# }
#
# print(len(mydic))
#
# mydic["color"] = "black"
#
# print(mydic)


# #Example8: Remove items from Dictionary:
#
# mydic = {'brand': 'Hyundai', 'model': 'i10', 'year': 2021, 'color': 'black'}
#
# print(mydic)
#
# #Use pop()
# mydic.pop("year")
# print(mydic)
#
#
# #del
# del mydic["color"]
# print(mydic)
#
# #clear()
# mydic.clear()
# print(mydic)
#
#
# del mydic
#
# print(mydic)


#Example9: Copy Dictionary

mydic = {'brand': 'Hyundai', 'model': 'i10', 'year': 2021, 'color': 'black'}
print(mydic)

mydic2 = mydic
print(mydic2)

# mydic3=mydic[::-1]        #Invalid - TypeError: unhashable type: 'slice'
# print(mydic3)

