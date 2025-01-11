import math
x = float(input('Введите значение x: '))
t = float(input('Введите значение t: '))
y = (1+x**2-2*x*t)/math.sin(t) + 1 + (1+(math.sin(x))**2 + (math.cos(x*t))**2)**(1/3)
print(y)