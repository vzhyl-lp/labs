from math import *

# Варіянт 8
# Таблиця 2

a = -1
b = -0.9
h = 0.01
d = 0.001

for i in range(int(round((b - a) / h)) + 1):

    x = round(i * h + a, 2) # Параметр розрахунку

    k = 2
    S = 0 # Сума ряду
    argS = ((-1)**k)*cos(k*x) / (k**2 - 1) # Черговий член ряду

    while abs(argS) > d:

        argS = ((-1)**k) * cos(k*x) / (k**2 - 1)
        S += argS
        k += 1

    print(x,":", S)