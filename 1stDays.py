class Person:
    def __init__(self, name, age):
        self.fname= name
        self.age= age
    def __str__(self):
         return f"{self.fname}({self.age})"
class Students(Person):
    def __init__(self, name, age,dept):
        super().__init__(name, age)
        self.dept = dept
p1 = Students("Atikur", 25, 2015)
print(p1.dept)