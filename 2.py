#pflfybt 3
n = int(input("Введите кол-во чисел: "))
q = 0
d = 0

for i in range (1, n + 1):
    if i % 2 == 0:
        q += 1
    else:
        d += 1

print("четных чисел: " , q)
print("нечетных чисел: " , d)