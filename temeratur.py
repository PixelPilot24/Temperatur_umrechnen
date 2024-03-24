# TODO testen
class Converter:
    @staticmethod
    def kelvin_input(temperature):
        celsius_var = temperature - 273.15
        fahrenheit_var = temperature * (9 / 5) - 459.15
        print(str(celsius_var) + " °C\n" + str(fahrenheit_var) + " °F")

    @staticmethod
    def celsius_input(temperature):
        kelvin_var = temperature + 273.15
        fahrenheit_var = temperature * (9 / 5) + 32
        print(str(kelvin_var) + " °K\n" + str(fahrenheit_var) + " °F")

    @staticmethod
    def fahrenheit_input(temperature):
        celsius_var = (temperature - 32) * (5 / 9)
        kelvin_var = (temperature + 459.67) * (5 / 9)
        print(str(celsius_var) + " °C\n" + str(kelvin_var) + " °K")

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
