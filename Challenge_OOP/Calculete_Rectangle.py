#!/usr/bin/env python3
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
        width=10
        lenght=10
        
    def enter_side(self):
        print('Width:{} and Length:{}'.format(self.width,self.length))

    def calculate_perimeter(self):
        perimeter = 2*(self.width + self.length)
        print(perimeter)

my_rectangle = Rectangle(100,50)        
my_rectangle.enter_side()
my_rectangle.calculate_perimeter()

