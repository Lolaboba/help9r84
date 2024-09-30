#Задание2
a = int(input("Начальный член: "))
r = int(input("Знаменатель: "))
n = int(input("Кол-во: "))
q = 1

for i in range (a , n + 1):
    a1 = a * (r ** (i - 1))
    print(a1)