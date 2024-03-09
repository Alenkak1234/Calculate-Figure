def calculate_circle(radius = None):
    if radius:
        return radius ** 2 * 3.1415926

def calculate_triangle(a = None, b = None, c = None):
    if a and b and c:
        p = 1/2 * (a + b + c)
        return (p * (p - a) * (p - b) * (p - c)) ** (1/2)


def calculate_square(type=None, **kwargs):
    '''Calculates square of a figure
    Parameters:
        type of a figure (str)
    Returns:
        square(int)
    '''
    if type == 'circle':
        return calculate_circle(**kwargs)
    if type == 'triangle':
        return calculate_triangle(**kwargs)



