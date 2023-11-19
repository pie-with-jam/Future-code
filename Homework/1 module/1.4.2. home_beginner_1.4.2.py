# Напишите программу, которая вводит следующие параметры (все они являются натуральными числами):
#
# cell – ширина ячейки в символах;
# cells – количество ячеек в строках;
# row – высота ячейки в символах;
# rows – количество строк.
# Используя арифметические операции со строками, программа должна построить фигуру-прямоугольник из ячеек (см. пример)

# *---*---*---*---*---*
# |   |   |   |   |   |
# |   |   |   |   |   |
# *---+---+---+---+---*
# |   |   |   |   |   |
# |   |   |   |   |   |
# *---+---+---+---+---*
# |   |   |   |   |   |
# |   |   |   |   |   |
# *---+---+---+---+---*
# |   |   |   |   |   |
# |   |   |   |   |   |
# *---*---*---*---*---*

cell=int(input())
cells=int(input())
row=int(input())
rows=int(input())

s1 = "*" + "-" * cell # *---
s2 = "|" + " " * cell # |

s3 = s1 * cells + "*\n" # *---*---*---*---*---*
s4 = s2 * cells + "|\n" # | | | | | |

s5 = "+" + "-" * cell # +---
s6 = s1 + s5 * (cells - 1) + "*\n" # *---+---+---+---+---*

s = s3 + (s4 * row + s6) * (rows - 1) + s4 * row + s3

print(s)