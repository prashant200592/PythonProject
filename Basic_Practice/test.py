list = [1, 0,5, "Prashant", 'a', True]
print (list)
list.reverse()
print (list)

for x in list:
    print (x)

tup = (2, 5.0, "Python", 'P', False)
print (tup)

for y in tup:
    print (y)

set = {0,2,2,1,5,1000,10, 100, 10}
print(set)

for a in set:
    print(a)

dict = {'Prashant':"Python", 'Aanna':"Selenium", 'Barkya':"UPSC", 'Gana':"SAAS", 'Swap':"PhD"}
print (dict)

print(dict.values())
print(dict.keys())

i = int(input("Enter positive number: "))

if i%2==0:
    print("You entered even number")

else:
    print("You entered odd number")

for j in range (1,100):
    if j%2==0:
        print(j,"Even number")
        break
    else:
        print(j, "Odd number")
        j+=1

for k in range(1,10):
    if k%2==0:
        print(k, "It's even number")
    else:
        print(k, "It's odd numer")
        k+=1

