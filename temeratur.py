import math


class Converter:
    @staticmethod
    def ceil_two_digit(num) -> str:
        num = math.ceil(num * 100) / 100
        return str(num)

    @classmethod
    def kelvin_input(cls, temperature):
        celsius_var = cls.ceil_two_digit(temperature - 273.15)
        fahrenheit_var = cls.ceil_two_digit(temperature * 1.8 - 459.67)
        print(celsius_var + " °C\n" + fahrenheit_var + " °F")

    @classmethod
    def celsius_input(cls, temperature):
        kelvin_var = cls.ceil_two_digit(temperature + 273.15)
        fahrenheit_var = cls.ceil_two_digit(temperature * 1.8 + 32)
        print(kelvin_var + " °K\n" + fahrenheit_var + " °F")

    @classmethod
    def fahrenheit_input(cls, temperature):
        celsius_var = cls.ceil_two_digit((temperature - 32) * (5 / 9))
        kelvin_var = cls.ceil_two_digit((temperature + 459.67) * (5 / 9))
        print(celsius_var + " °C\n" + kelvin_var + " °K")

    @classmethod
    def get_temp(cls):
        print("\nMit \"beenden\" wird das Programm beendet.")
        while True:
            unit = input("Welche Einheit soll umgerechnet werden C, K, F: ")
            unit_list = ["C", "c", "K", "k", "F", "f", "beenden"]

            if unit in unit_list:
                if unit == "beenden":
                    break

                print("Mit \"zurück\" gelangt man zur Einheitenauswahl")

                while True:
                    temperature = input("Gib die Temperatur ein: ")

                    if temperature == "zurück":
                        break

                    try:
                        temperature = float(temperature)

                        if unit == "C" or unit == "c":
                            cls.celsius_input(temperature)
                        elif unit == "K" or unit == "k":
                            cls.kelvin_input(temperature)
                        else:
                            cls.fahrenheit_input(temperature)
                    except ValueError:
                        print("Der eingegebene Wert muss eine Zahl sein")

            else:
                print("Die Eingabe war nicht korrekt")


if __name__ == "__main__":
    Converter.get_temp()
