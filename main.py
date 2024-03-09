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

    def calculate_square(self, **kwargs):
        if self.type == 'circle':
            return self.calculate_circle(**kwargs)
        elif self.type == 'triangle':
            return self.calculate_triangle(**kwargs)

    def calculate_circle(self, radius=None):
        if radius:
            return radius ** 2 * 3.1415926

    def calculate_triangle(self, a=None, b=None, c=None):
        if a and b and c:
            p = 1 / 2 * (a + b + c)
            return (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)


figure = Figure('circle')
square = figure.calculate_square(radius=2)
print(square)
figure = Figure('triangle')
square = figure.calculate_square(a=4, b=4, c=2)
print(square)
