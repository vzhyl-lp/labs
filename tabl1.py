from math import *

# Варіянт 8
# Таблиця 1

a = 1.5
b = 3.5
h = 0.2

for i in range(int(round((b-a) / h) + 1)):
    
    # Вводимо параметр х для розрахунку
    x = i*h + a

    #Результат розрахунку
    f = 0

    lim1 = 2
    lim2 = 3

    if x < lim1:
        # Косеканс
        f = sin(exp(x))**(-1) 

    elif lim1 <= x < lim2:
        # Секанс
        f = cos(log(x))**(-1)

    elif x >= lim2:
        f = sin(log(x))

    print(x, ":", f)