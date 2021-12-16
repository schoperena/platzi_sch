import PySimpleGUI as sg


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

    car_1 = []

    main_window_layout = [
        [sg.Text("ingrese los datos:")],
        [sg.Text("Modelo:"), sg.InputText(s=(20,10), expand_x=True, do_not_clear=False, focus=True, tooltip="Ingrese el modelo")],
        [sg.Text("Marca: "), sg.InputText(s=(20,10), expand_x=True, do_not_clear=False, tooltip="Ingrese la marca")],
        [sg.Text("Color:  "), sg.InputText(s=(20,10), expand_x=True, do_not_clear=False, tooltip="Ingrese el color")],
        [sg.Checkbox("Airbag", default=False)],
        [sg.Button("Ok"), sg.Button("Cerrar")]
    ]

    try:

        window = sg.Window("Car Generator", main_window_layout, keep_on_top=True, no_titlebar=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Cerrar":
                break

            for i in values:
                car_1.append(values[i])

        window.close()

        # instance creatin (model, car, color, airbag(True or False))
        car_1 = Car(car_1[0], car_1[1], car_1[2], car_1[3])

        car_1.acceleration("stop")

        # print car info
        car_1.car_satus()

    except IndexError:
        print("No dejar los campos vacios")


if __name__ == '__main__':
    main()
