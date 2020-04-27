class Ksztalty:
    def __init__(self,x):
        self.x = x
        
    def __gt__(self, liczba):
        return self.x > liczba.x

    def __ge__(self, liczba):
        return self.x >= liczba.x

    def __lt__(self, liczba):
        return self.x < liczba.x

    def __le__(self, liczba):
        return self.x <= liczba.x

class Kwadrat(Ksztalty):
    def __gt__(self, zxc):
        return self.x > zxc.x

x1 = Ksztalty(20)
x2 = Ksztalty(21)

print(x1.__gt__(x2))
print(x1.__ge__(x2))
print(x1.__lt__(x2))
print(x1.__le__(x2))

x3 = Kwadrat(21)
x4 = Kwadrat(53)

print(x3.__gt__(x4))