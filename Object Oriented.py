#########
# Loops #
#########

class Employee:
    # Class Variable
    empCount = 0

    # instantiate with name and salary
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # A method
    def displayCount(self):
        print "Total Employees: " + str(Employee.empCount)

    def displayEmployee(self):
        print "Name: " + str(self.name) + ", Salary: " + str(self.salary)

# Instantiate and Using Methods
emp1 = Employee("Jane", 2000)
emp1.displayCount()
emp1.displayEmployee()

#Access Class Variabe
print Employee.empCount
