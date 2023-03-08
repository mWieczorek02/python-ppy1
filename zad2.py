class Person:
   def __init__(self, name, height, hair_color, eye_color):
       self.name = name
       self.height = height,
       self.hair_color = hair_color,
       self.eye_color = eye_color

    def __str__(self):
        return f"name: {self.name}\nheight: {self.height}\nhair color: {self.hair_color}\neye color: {self.eye_color}\n\n"

people = []

def print_people():
    for person in people:
        print(f"name: {person.name}\nheight: {person.height}\nhair color: {person.hair_color}\neye color: {person.eye_color}\n\n")

def add_person():
    name = input("input name")
    height = input("input height")


def main():
    operation = input("choose operation: print/add")
    match operation:
        case "print":
            print_people()
        case "add":





if __name__ == "__main__":
    print()