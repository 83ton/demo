# Citim de la tastatura 3 valori intregi: a, b si c care ne descriu
# o ecuatie de gradul doi. Vrem sa aflam solutiile acestei ecuatii si
# sa aflam coordonatele punctului de minim sau de maxim al functiei
# aferente acestei ecuatii.
import math

a = int(input("Introduceti valoarea pentru a:"))
b = int(input("Introduceti valoarea pentru b:"))
c = int(input("Introduceti valoarea pentru c:"))

# a * (x ^ 2) + b * x + c = 0
# delta = b ^ 2 - 4 * a * c
# x1,2 = (-b +- sqrt(delta)) / 2a

x1 = -99999999
x2 = -99999999

delta = b * b - 4 * a * c
if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

print(x1, x2)

max_point = list()
min_point = list()

if a > 0:
    min_point.append(-b / (2 * a))
    min_point.append(-delta / 4 * a)
    print(min_point)
elif a < 0:
    max_point.append(-b / (2 * a))
    max_point.append(-delta / 4 * a)
    print(max_point)