import math


def quadratic_equation(a, b, c):
    delta = math.sqrt(b ** 2 - 4 * a * c)

    x1 = (-b + delta) / 2 * a
    x2 = (-b - delta) / 2 * a

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
