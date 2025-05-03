import math

class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def plus(self):
        suma = self.first_number + self.second_number
        print(suma)

    def minus(self):
        ryznitsa = self.first_number - self.second_number
        print(ryznitsa)

    def mnozh(self):
        mnozh = self.first_number * self.second_number
        print(mnozh)

    def dilenya(self):
        if self.second_number !=0:
            dilenya = self.first_number / self.second_number
            print(dilenya)
        else:
            print("Дія  неможлива")

    def descruminant(self, a, b, c):
        d =  b**2 - 4*a*c
        if d > 0:
            x1 = (-b + math.sqrt(d) / 2 * a)
            x2 = (-b - math.sqrt(d) / 2 * a)
            print(f"X1= {x1}" f"X2= {x2}")
        if d == 0:
            print("Пуста множина")



a = Calculator()
a.descruminant( a, b, c)
