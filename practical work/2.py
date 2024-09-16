import math
#2 пример
x = -4.5
y = 0.75 * (10 ** -4)
z = -0.845 * (10 ** 2)

s = (((9 + (x - y) ** 2) ** (1/3)) / (x ** 2 + y ** 2 + 2))  - math.exp(math.fabs(x - y)) * (math.tan(z)) ** 3

g=round(s, 5) 
print(g)