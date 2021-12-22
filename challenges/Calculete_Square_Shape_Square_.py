class Shape():
    def what_am_i(self):
        print('Я - фигура.')
    
class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
        
    def change_size(self, lenght):
        self.lenght = lenght
    
    def calculate_area(self):
        self.i = 4 * self.lenght
        print('Периметр равен =', self.i, 'метрам')

        
    def print_size(self):
        print("I am a square that is {} by {}".format(self.width, self.length))

my_square = Square(20)
my_square.change_size(10)
my_square.calculate_area()
my_square.call()

my_shape = Shape()
my_shape.call()
