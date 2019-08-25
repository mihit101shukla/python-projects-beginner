import math


def quad_solutions(a, b, c):
    if (b * b) - (4 * a * c) < 0:
        return('NO REAL SOLUTIONS')
    else:

        x = (-b + math.sqrt((b*b) - (4*a*c))) / (2*a)
        y = (-b - math.sqrt((b*b) - (4*a*c))) / (2*a)
    print(f'x = {x} and x = {y}')


quad_solutions(1, 5, 6)
