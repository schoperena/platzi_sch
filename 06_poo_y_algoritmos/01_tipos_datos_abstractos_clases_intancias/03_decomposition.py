import os


class Car:

    def __init__(self, model, brand, color, airbag):
        self.model = model
        self.brand = brand
        self.color = color
        self.airbag = Airbag(airbag)
        # private variables
        self._status = 'moving'
        self._engine = Engine(cylinders=4)

    def acceleration(self, type):
        if type == 'fast':
            self._engine.petrol_injection(10)
        elif type == 'slow':
            self._engine.petrol_injection(3)
        else:
            self._engine.petrol_injection(0)
            self._status = 'resting'

    def car_satus(self):
        print(
            f"""
        the {self.color} {self.brand} {self.model}, is {self._status}. 
        the engine has {self._engine.status()[0]} cylinders that use {self._engine.status()[1]},
        with a petrol injection amount of {self._engine.status()[2]}.
        The airbag is {self.airbag.status()}.
        """
        )


class Engine:

    def __init__(self, cylinders, type='petrol'):
        self.cylinders = cylinders
        self.type = type
        self._temp = 0

    def petrol_injection(self, amount):
        self._amount = amount

    # return Engine specs
    def status(self):
        return self.cylinders, self.type, self._amount


class Airbag:

    def __init__(self, operation):
        self.operation = operation

    # Return airbag status
    def status(self):
        if self.operation == True:
            return 'on'
        else:
            return 'off'


def main():

    os.system("cls")

    # instance creatin (model, car, color, airbag(True or False))
    car_1 = Car("Corolla", "Toyota", "gray", True)
    car_2 = Car("Focus", "Ford", "red", False)
    car_3 = Car("Cerato", "Kia", "green", True)

    car_1.acceleration("stop")
    car_2.acceleration("fast")
    car_3.acceleration("slow")

    # print car info
    car_1.car_satus()
    car_2.car_satus()
    car_3.car_satus()


if __name__ == '__main__':
    main()
