from math import sqrt, sin


def circle_square(r):
    return r * r * 3.1415


def triangle_square_3sides(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def triangle_square_angle(a, b, alpha, degree=True):
    if degree:
        alpha = alpha * 3.1415 / 180
    return (a * b * sin(alpha)) / 2


def rectangle_square(a, b):
    return a * b
