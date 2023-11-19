import random

def getSum(n):
    sum = 0

    while (n != 0):
        sum = sum + n % 10
        n = n // 10

    return sum

a = random.randint(100, 999)
print(f"Сумма цифр числа {a} равна {getSum(a)}")