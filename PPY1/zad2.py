# Mikołaj Wieczorek s24697

class Person:
    def __init__(self, name: str, height: str, hair_color: str, eye_color: str):
        self.name = name
        self.height = height,
        self.hair_color = hair_color,
        self.eye_color = eye_color


people = [
    Person("Mikolaj", "183", "brown", "brown")
]


def print_people():
    for person in people:
        print(
            f"name: {person.name}, height: {person.height}, hair color: {person.hair_color}, eye color: {person.eye_color}")


def add_person():
    name = input("input name ")
    height = input("input height ")
    hair_color = input("input hair color ")
    eye_color = input("input eye color ")
    people.append(Person(name, height, hair_color, eye_color))
    print(f"successfully added person with name {name}")


def main():
    flag = True
    while flag:
        operation = input("choose operation: print/add/stop ")
        match operation:
            case "print":
                print_people()
            case "add":
                add_person()
            case "stop":
                flag = False


if __name__ == "__main__":
    main()
