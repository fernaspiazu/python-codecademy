__author__ = 'fumandito'


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return (hours / 2) * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


print Employee("Arnold").calculate_wage(8)
print PartTimeEmployee("Mike").calculate_wage(8)
print PartTimeEmployee("Milton").full_time_wage(10)
