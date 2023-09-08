class Rectangle:
    pass

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (2*self.length) + (2*self.width)

    def is_square(self):
        if self.width == self.length:
            return True
        else:
            return False

shape1 = Rectangle(5, 3)
shape2 = Rectangle(10, 9)
shape3 = Rectangle(4, 4)

# Example Usage
print(shape2.get_perimeter())
print(shape3.is_square())
print(shape1.is_square())
print(shape3.get_area())
