
class Student:

    def __init__(self,rn,sname,fees):
        self.rn=rn
        self.sname=sname
        self.fees=fees

    def display(self):
        print(self.rn,self.sname,self.fees)

# stu = Student(42, "Prash", 500)
# stu.display()