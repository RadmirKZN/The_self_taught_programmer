#1
class Apple():
   def __init__(self, x, y, w, z):
        self.weight = y
        self.circle = w
        self.flavor =z
apple=Apple(3, 4, 5, 37)
print(apple.circle)

#2
import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
a_circle = Circle(10)
print(a_circle.calculate_area())
#3
import math

class Triangle():
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def calculate_area(self):
        return self.height * self.base / 2
S_triangle=Triangle(50,100)
print(S_triangle.calculate_area())
#4
class Hexagon():
    def __init__(self, side):
        self.side=side

    def calculate_area(self):
        return self.side * 6
S_hexagon=Hexagon(10)
print(S_hexagon.calculate_area())




        
 
