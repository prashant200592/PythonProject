#Approach1:
# import a
# import b
#
# obj1 = a.Animal()
# obj1.display()
#
# obj2 = b.Bird()
# obj2.display()

#Approach2:
from a import Animal
obj1 = Animal()
obj1.display()

from b import Bird
obj2 = Bird()
obj2.display()



