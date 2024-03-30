from abc import ABC, abstractmethod


class Figures(ABC):
    @abstractmethod
    def calculate_square(self):
        pass


class Figure(Figures):
    """Class square of a figure
        Parameters:
            type of figure (str)
            necessary data to calculate
        Returns:
            square(int)
        """

    def __init__(self, type):
        self.type = type

    @staticmethod
    def check_rectangular(a=None, b=None, c=None):
        max_number = max(a, b, c)
        min_number = min(a, b, c)
        ost_number = a + b + c - max_number - min_number
        if max_number ** 2 == min_number ** 2 + ost_number ** 2:
            return 'равнобедренный'
        else:
            return 'неравнобедренный'

    def calculate_square(self, **kwargs):

        if self.type == 'круг':
            radius = float(input('Введите радиус круга\n)'))
            return self.calculate_circle(radius=radius)

        elif self.type == 'треугольник':
            a = float(input('Введите 1-ую сторону треугольника\n'))
            b = float(input('Введите 2-ую сторону треугольника\n'))
            c = float(input('Введите 3-ую сторону треугольника\n'))
            if a + b > c and a + c > b and b + c > a:
                return self.calculate_triangle(a = a, b = b, c = c)
            else:
                return "Треугольник не существует"


    def calculate_circle(self, radius=None):
        if radius:
            return radius ** 2 * 3.1415926

    def calculate_triangle(self, a=None, b=None, c=None):
        if a and b and c:
            p = 1 / 2 * (a + b + c)
            return (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)



