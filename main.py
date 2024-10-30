# Варіянт 8
# Чи є рядок капсом?

# Вбудований метод - isupper()


UP_ALPH = list(map(chr, range(65, 91))) + [" "]

L = [1,2,3]
L.clear()
print(L)

print(UP_ALPH)

def is_uppercase (str):
    isUpBoolean = True
    
    for str_ch in str:
        if str_ch in UP_ALPH:
            continue
        else:
            isUpBoolean = False
    
    print(f"\"{str}\" is uppercase:", isUpBoolean)

is_uppercase(input("Your text: "))


# Питання

# 1. Список - це набір елементів. Пустий список має довжину 0

# 2. append(<el>), 
# insert(<i>, <el>)
# List1.extend(List2)

# 3. pop( <el pos> ) або remove( <element> )

# 4. print(L[i])

# 5. L[3:10] - від 3 до 10, можна з кроком L[4:10:2]

# 6. Кортеж - через (), як список, але не змінюється

# 7. Dict = {
#   <key>: <val>,
#   <key>: <val>
#   ...
# }
# 
# print(Dict["<key>"])

# 8. Dict["<new key>"] = "new val"
# Dict.pop(<i>)

# 9. print(Dict["<key>"])

# 10. mySet = {"<el>", "<el>", ...}
# Невпорядкований, незмінні елементи, немає індексів, не можуть повторюватися

# 11. mySet.add(<el>)
# mySet.remove(<el>)

# 12. <el> in mySet
# Якщо є, результат - True

# 13. 
# def myFunction(x):
#   <func code>

# 14. def myFunction(<arg>):
#       <func code>

# 15. return <expression>

# 16.
# a = lambda x : x + 10
# print(a(10))

# 17. len(myList)
# sum(myList)

# 18. List comprehensions

# print([el*2 for el in range(0,15) if not el % 2])