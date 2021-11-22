class persegipanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l
    def keliling(self):
        return 2 * (self.p + self.l)
    def luas(self):
        return self.p * self.l
pp = persegipanjang(10, 5)
print(pp.keliling())
print(pp.luas())
