class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def enter_side(self):
        print('Width:{} and Length:{}'.format(self.width,self.length))

    def calculate_perimeter(self):
        perimeter = 2*(self.width+self.length)
        print(perimeter)
        

my_rectangle = Rectangle(50, 100)
my_rectangle.enter_side()
my_rectangle.calculate_perimeter()
