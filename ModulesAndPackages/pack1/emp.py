
class Employee:

    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def display(self):
        print(self.eid, self.ename,self.sal)


# emp = Employee(20389,"Prashant",150000)
# emp.display()