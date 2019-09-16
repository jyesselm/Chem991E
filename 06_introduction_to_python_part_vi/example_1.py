class Parent:
    def func(self):
        return 10


class Child1(Parent):
    def func(self):
        #python 3.x
        return super().func()*10


class Child2(Child1):
    def func(self):
        return super().func()*10


c = Child1()
c2 = Child2()
print(c.func())
print(c2.func())