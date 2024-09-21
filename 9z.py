import math

class Frac:
    def __init__(self,upnumber: int,downnumber: int):
        if downnumber == 0:
            raise ValueError("Знаменатель не должен быть 0")
        self.upnumber = upnumber
        self.downnumber = downnumber
        self._simplify()
    def _simplify(self):
        greatcd = math.gcd(self.upnumber, self.downnumber)
        self.upnumber //= greatcd
        self.downnumber //= greatcd
    def __str__(self):
        return f"{self.upnumber}/{self.downnumber}"
    def obrat(self): #?inverse?
        return Frac(self.downnumber,self.upnumber)
    def __add__(self, other):
        new_upnumber = ((self.upnumber * other.downnumber) + (self.downnumber * other.upnumber))
        new_downnumber = (self.downnumber * other.downnumber)
        return Frac(new_upnumber, new_downnumber)
    def __mul__(self, other):
        new_up = self.upnumber * other.upnumber
        new_down = self.downnumber * other.downnumber
        return Frac(new_up, new_down)

frac0 = Frac(1,2)
frac1 = Frac(3,4)
frac2 = Frac(2,1)

obrat_frac0 = frac0.obrat()
print(obrat_frac0)

sum_frac = frac1 + frac0
print(sum_frac)

multiply_frac = frac0 * frac2
print(multiply_frac)

