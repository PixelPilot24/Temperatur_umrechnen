def kelvin(celsius=0):
    return str(celsius + 273.15)


def celsius(kelvin=-273.15):
    return kelvin - 273.15


def get_temp():
    while True:
        C = input("Gib die Temperatur in Grad Celsius ein: ")
        try:
            C = float(C)
            print("Die Temperatur beträgt: " + kelvin(C) + "°K")
            break
        except ValueError:
            print("Die Eingabe darf nur eine Zahl sein")


if __name__ == "__main__":
    get_temp()
