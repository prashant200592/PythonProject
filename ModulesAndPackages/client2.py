
import sys
sys.path.append("C:/Users/Megha Kadam/PycharmProjects/pythonProject/ModulesAndPackages/package1")
sys.path.append("C:/Users/Megha Kadam/PycharmProjects/pythonProject/ModulesAndPackages/package1/package2")

#Approach1:
# import module1
# module1.display()
#
# import module2
# module2.show()



#Approach2:
from module1 import *
from module2 import *

display()
show()



