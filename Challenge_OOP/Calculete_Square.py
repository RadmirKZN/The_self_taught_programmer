class Shape():
    def call(self):
        print('Я - фигура.')
    
class Square(Shape):
    
    square_list = []
    
    def __init__(self, lenght):
        self.lenght = lenght
        self.square_list.append((self.lenght))
        
    def change_size(self, lenght):
        self.lenght = lenght
    
    def calculate_area(self):
        self.i = 4 * self.lenght
        print('Периметр равен =', self.i, 'метрам')
    def print_side(self):
        print(self.lenght, ' HA ', self.lenght,   ' HA', self.lenght,  ' HA ', self.lenght) 

my_square = Square(20)
my_square = Square (404)
print( Square.square_list)
my_square.print_side()
