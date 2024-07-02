class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive")


# Creating person to see if they can drive from inputs
def create_person():
    name = "Jess"
    age = 20
    eye_color = "blue"
    hair_color = "red"

    # If person reaches requirements they can drive and not they can not
    if age >= 18:
        person = Adult(name, age, eye_color, hair_color)
        person.can_drive()
    else:
        person = Child(name, age, eye_color, hair_color)
        person.can_drive()


create_person()