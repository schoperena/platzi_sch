
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes ingresar cadenas"
        return string * n
    return repeater


if '__main__' == __name__:
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))
