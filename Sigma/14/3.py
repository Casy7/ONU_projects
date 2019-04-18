class Figure():
    def __init__(self, *sides):
        self.sides = sides

    def perimether(self):
        P = 0
        for side in self.sides:
            P += side
            
class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        P = self.side1 + self.side2 + self.side3
        return P

    def square(self):
        p = self.perimeter()/2
        a = self.side1
        b = self.side2
        c = self.side3
        return (p*(p-a)*(p-b)*(p-c))**0.5

    @property
    def name(self):
        return "Triangle"


class Rectangle(Figure):
    def __init__(self, lenth, height):
        self.lenth = lenth
        self.height = height
        # super().__init__(sides)

    def perimeter(self):
        P = 2*self.lenth+2*self.height
        return P

    def square(self):
        S = self.lenth*self.height
        return S

    @property
    def name(self):
        return "Rectangle"


class Trapezoid(Figure):
    def __init__(self, a, b, c, d, height):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height
        # super().__init__(sides)

    def perimeter(self):
        P = self.a+self.b+self.c+self.d
        return P

    def square(self):
        S = (self.a*self.c)/2*self.height
        # h=a+b2√c2−((b−a)2+c2−d22(b−a))2
        return S

    @property
    def name(self):
        return "Trapezoid"


#poly = Figure(9,8,7,9,8,0,7)
triang = Triangle(3, 4, 5)
rect = Rectangle(4, 5)
trapecya = Trapezoid(4, 4, 8, 12, 10)

polygons = [triang, rect, trapecya]

for polyg in polygons:
    print(f"Square of {polyg.name}: {polyg.square()}")
    print(f"Perimeter of {polyg.name}: {polyg.perimeter()}")
