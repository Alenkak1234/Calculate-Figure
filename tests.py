import unittest
from main import Figure


class TestFigure(unittest.TestCase):
    def setUp(self):
        self.figure = Figure('circle')

    @staticmethod
    def test_check_rectangular(a=None, b=None, c=None):
        max_number = max(a, b, c)
        min_number = min(a, b, c)
        ost_number = a + b + c - max_number - min_number
        if max_number ** 2 == min_number ** 2 + ost_number ** 2:
            return 'равнобедренный'
        else:
            return 'неравнобедренный'

    def test_calculate_square(self, **kwargs):
        if self.type == 'circle':
            self.figure.calculate_circle(**kwargs)
        elif self.type == 'triangle':
            return self.calculate_triangle(**kwargs)

    def test_calculate_circle(self, radius=None):
        if radius:
            return radius ** 2 * 3.1415926

    def test_calculate_triangle(self, a=None, b=None, c=None):
        if a and b and c:
            p = 1 / 2 * (a + b + c)
            return (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
