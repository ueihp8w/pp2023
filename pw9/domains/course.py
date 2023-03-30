from .entity import Entity

class Course(Entity):
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self.credit = credit

    def __str__(self):
        return f"{self.id:<12}{self.name:<12}{self.credit}"