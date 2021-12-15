
class WasherMachine:

    def __init__(self):
        pass

    def wash(self, temp="hot"):
        self._fill_tank(temp)
        self._add_soap()
        self._wash()
        self._spin_dry()

    def _fill_tank(self, temp):
        print(f"Fillin tank with {temp} water")

    def _add_soap(self):
        print("Adding soap")

    def _wash(self):
        print("Washing")

    def _spin_dry(self):
        print("Spinning")

def main():
    washer_1 = WasherMachine()
    washer_1.wash()


if __name__ == "__main__":
    main()