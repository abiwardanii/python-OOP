class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height * 3.14 * self.radius ** 2
    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())