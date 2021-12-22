class Shape():
	def __init__(self,w, x ):
	    self.width=w
	    self.len=x

	def print_size(self):
		print("""{} by {}
			  """.format(self.width,
			  	         self.len))
class Square(Shape):

        def print_size(self):
                print("""Я {} на {}
              """.format(self.width, 
                             self.len)) 
        

a_square = Square(100,100)
a_square.print_size()
print()
print()
print()
class Dog():
        def __init__(self, name, breed, owner):
            self.name=name
            self.name=breed
            self.owner=owner
class Person():
        def __init__(self, name):
            self.name=name


mick=Person('Мик Джаггер')
stan=Dog('Stenly','Buldog',mick)
print(stan.owner.name)
            
