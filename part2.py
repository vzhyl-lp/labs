from math import cos as vadym


# ТАБЛИЦЯ 1

# Змінні
movie = "Індіана Джонс"
print("Улюблений фільм: ", movie)


# Оператори порівняння
is_employee = False
is_employer = True

print("Не дорівнює: ", (is_employee != is_employer))


# Булеві оператори
is_sunny = True
is_raining = False

print("Логічне не. Сонячно: ", not is_sunny, "; ",
      "Йде дощ: ", not is_raining)



# ТАБЛИЦЯ 2

z = 9.761

print("Результат виразу: ", 
      (pow(z, 6) + 13*pow(z, 4) + 7*pow(z, 3) + 14*pow(z, 2) - 2*z + 21)*vadym(z))

# Або
# z**6 + 13*(z**4) + 7*(z**3) + 14*(z**2) - 2*z + 21