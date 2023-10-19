class Circle:
    def __init__(self, radius):
        self.rad = radius

    def __eq__(self, radius2):
        return self.rad == radius2.rad

    def __lt__(self, radius2):
        return self.rad < radius2.rad

    def __gt__(self, radius2):
        return self.rad > radius2.rad

    def __le__(self, radius2):
        return self.rad <= radius2.rad

    def __ge__(self, radius2):
        return self.rad >= radius2.rad

    def __iadd__(self, number):
        self.rad = self.rad + number

    def __isub__(self, number):
        self.rad = self.rad - number

cir = Circle(5)
cir2 = Circle(6)

#print(cir == cir2)

class Airplane:
    def __init__(self, count_of_passengers):
        self.pas = count_of_passengers

    def __eq__(self, count_of_passengers):
        return self.pas == count_of_passengers.pas

    def __lt__(self, count_of_passengers):
        return self.pas < count_of_passengers.pas

    def __gt__(self, count_of_passengers):
        return self.pas > count_of_passengers.pas

    def __le__(self, count_of_passengers):
        return self.pas <= count_of_passengers.pas

    def __ge__(self, count_of_passengers):
        return self.pas >= count_of_passengers.pas

    def __iadd__(self, number):
        self.pas = self.pas + number

    def __isub__(self, number):
        self.pas = self.pas - number

plane1 = Airplane(200)
plane2 = Airplane(150)
#print(plane1 == plane2)









