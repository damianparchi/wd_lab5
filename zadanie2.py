class Kwadrat():
    def __init__(self,x):
        self.x=x
        self.y=x

    def __add__(self,drugi):
        return (self.x + drugi.x)


square = Kwadrat(14)
square2 = Kwadrat(11)
wynik= square.__add__(square2)
print(wynik)
