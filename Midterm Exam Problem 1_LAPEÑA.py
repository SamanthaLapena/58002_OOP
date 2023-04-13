class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def perimeter(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * self.radius ** 2

    def display(self):
        print("Area of the circle:", self.area())
        print("Perimeter of the circle:", self.perimeter())

circle = Circle(float(input("Radius of the circle:")),3.14)
circle.display()