# Напишите программу, которая считывает произвольный и ''рисует'' им следующую фигуру (нули в качестве символов взяты ради примера):
#
# 0   0
# 00 00
#  000
# 0 0 0

symbol = str(input())

print(symbol, symbol, sep=" " * 3)
print(symbol * 2, symbol * 2, sep=" ")
print(" ", " ", sep=symbol * 3)
print(symbol, symbol, symbol, sep=" ")