import math
def square_triangle(a): 
    s_triangle = (a**2 * math.sqrt(3)) / 4 
    return s_triangle
def square_hexagon(a):
    return square_triangle(a) * 6 
a = int(input('введите длину стороны шестиугольника:'))

print(square_hexagon(a))