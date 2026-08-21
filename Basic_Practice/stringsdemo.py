#Create string variable

#Example1: Ways of creating string variables

# a="Welcome"
# b='to'
# c=str("Python")
# d=str('sessions')
#
# #Create empty string
# l=""
# m=''
# n=str()
#
# print(a,b,c,d)
# print(l,m,n)
#
# #Example2: String-Update value
# print(id(a))    #1923659484528
# a=a+"to Python"
# print(id(a))

# #Example3: + and * with string
#
# str1 = "Welcome"
# print(str1+" Programming")
# print(str1*5)

# #Example4: Slicing

# str="Welcome"
# print(str)
# print(str[1:3])
# print(str[:6])
# print(str[2:])
# print(str[1:-1])
# print(str[1:-2])

# #Example5: ord() and chr()
#
# print(ord('A'))
# print(chr(65))

# #Example6: max() || min() || len()
#
# print(max("welcome"))
# print(min("python"))
# print(len("WelcomeToPython"))


# #Example7: in and not in operatots - Returns True/False
#
# s = "Welcome"
# print("come" in s)
# print("lome" in s)
#
# print("come" not in s)
# print("lome" not in s)

# #Example8: String Comparison
#
# print("tim" == "tie")
# print("z" > "yellow")
# print("abc" > '')

# #Example9: Testing Strings  True/False
#
# s = "welcometopython"
#
# print(s.isalnum())
# print(s.isalpha())
# print("welcome".isalpha())
# print("12at".isalnum())
# print("123".isalnum())
#
# print(s.islower())
# print("234a".isdigit())
#
# print("1f2o3r".isidentifier())
#
# print("PRASHANTpsl".isupper())
#
# print(" 1".isspace())


# #Example10: Searching for substrings
#
# s = "Welcome to python"
#
# print(s.endswith("thon1"))
# print(s.startswith("Welc1"))
#
# print(s.find("come"))
#
# print(s.find("become"))
#
# print(s.count("t"))
''

# #Example11: Converting strings
#
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)
#
# s2 = s.title()
# print(s2)
#
# s3 = s.lower()
# print(s3)
#
# s4 = s.upper()
# print(s4)
#
# s5 = s.swapcase()
# print(s5)
#
# s6 = s.replace("in", "on")
# print(s6)



#Example12: Reverse a atring
#Method1

# s = "welcome"
# rev_str = ""
#
# for i in s:
#     rev_str=i+rev_str
#
# print("Reverse string of: ", s, "is", rev_str)

#Method2

# s = "Welcome"
# rev_str = s[::-1]
#
# print("Reverse string of: ", s, "is", rev_str)







s = "Prashant"
rev_str = s[::-1]
print("Reverse string of ", s, "is", rev_str)

rev_str = ""

for i in s:
    rev_str = i+rev_str

print("Reverse string of ", s, "is", rev_str)










