class Employee:
    name = ""
    age = 0
    department = ""

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def show(self):
        print "Employee: { Name: %s, Age: %s, Department: %s }" %  (self.name, self.age, self.department)

emp = Employee("Thai", 28, "ZBC")
emp.show()
print Employee.__module__
del emp