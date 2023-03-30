from .entity import Entity

class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def __str__(self):
        return f"{self.id:<12}{self.name:<15}{self.dob}"