class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        area = self.__side_length ** 2
        return area

    def info(self):
        return f'Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.'

class Rectangle(Figure):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def calculate_area(self):
        area = self.__width * self.__length
        return area

    def info(self):
        return (f'Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, '
                f'area: {self.calculate_area()}{Figure.unit}.')

figures = [Square(6), Square(9), Rectangle(4,7), Rectangle(6,8), Rectangle(9,10)]

for figure in figures:
    print(figure.info())
