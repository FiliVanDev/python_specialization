# Задание по программированию: Корни квадратного уравнения
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
print(a)
d = b * b - 4 * a * c
x1 = int((-b + math.sqrt(d)) / (2 * a))
x2 = int((-b - math.sqrt(d)) / (2 * a))

print(x1)
print(x2)