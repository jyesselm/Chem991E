# parent class
class Person:
    # Constructor
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Employee(Person):
    def __init__(self, first_name, last_name, age, pay, id_num):
        # invoking the __init__ of the parent class
        Person.__init__(first_name, last_name, age)

        self.pay = pay
        self.id_num = id_num


emp = Employee("Tom", "Ike", 30, 40000, 40925)
print(emp.get_full_name())

# output
# Tom Ike




