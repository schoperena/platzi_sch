
class Person:

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def saluda(self, other_person):
        return f"Hello {other_person.name}, i'm {self.name}"


def main():

    # instances creation
    david = Person('David', 35)
    erika = Person('Erika', 32)

    # method execution
    print(david.saluda(erika))


if __name__ == '__main__':
    main()
