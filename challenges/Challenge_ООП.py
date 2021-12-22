#1
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

class Square():
    def __init__(self, width, length):
       self.width=width
       self.leng=length

    def print_side(self):
        print('width:{} and Length{}'.format(self.width,self.length))

    def calculate_perimeter(self):
        perimeter = self.width * self.leng
        print(perimeter)


my_square = Square(100,100)
my_square.enter_side()
my_square.calculete_perimeter()  
#2
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(25)
print(a_square)
























