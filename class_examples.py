
"""
EXAMPLE OF CLASS-LEVEL ATTRIBUTES
class Player:
    MAX_POSITION = 10
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        self.steps = steps
        if self.position + self.steps < Player.MAX_POSITION:
            self.position = self.position + self.steps
        else:
            self.position = Player.MAX_POSITION
        return self.position

    # This method provides a rudimentary visualization in the console
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
"""


"""
EXAMPLE OF CLASSMETHODS

# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetimeobj):
      day = datetimeobj.day
      month = datetimeobj.month
      year = datetimeobj.year
      return  cls(year, month, day)

today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)
"""


"""
CLASS INHERIT ANOTHER CLASS

class Employee:
  MIN_SALARY = 30000

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
  def give_raise(self, amount):
    self.salary += amount

# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print("Manager" + self.name)

mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()
"""

"""
METHOD INHERITANCE AND POLYMORFISM

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        Employee.give_raise(self, amount * bonus)
"""

"""
STRING REPRESENTATION OF OBJECTS

class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
    # Add the __str__() method
    def __str__(self):
        f = "Employee name: {}, Employee salary: {}".format(self.name, self.salary)
        return f

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
"""
