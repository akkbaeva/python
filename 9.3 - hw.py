class Weather:

    def __init__(self, kind, degree):
        self.kind = kind
        self.degree = degree

    def sunny(self):
        return self.degree * 2

    def __str__(self):
        return f'{self.kind}, {self.degree}'

class Spring(Weather):
    def cloudy(self):
        return super().sunny() * 3

class Summer(Spring):
    def mainly_cloudy(self):
        return super().cloudy().sunny() * 2


po = Weather('wind', '10')
print(po)
print(po.sunny())
sp = Spring('rain', '5')
print(sp)
print(sp.cloudy())
su = Summer('sun', '15')
print(su)
print(su.sunny().mainly_cloudy())





    