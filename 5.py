#5 задание
n = int(input("Введите кол-во чисел: "))
z = 0
q = 1
j = 0
for i in range (1 , n + 1):
    z += i
    q *= i
    j = z / n
print("Сумма всех чисел: " , z , ", произведение всех чисел: " , q , ", среднее арифметическое чисел: " , j)