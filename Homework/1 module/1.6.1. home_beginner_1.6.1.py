# Считайте со стандартного потока ввода два целых числа. Выведите информацию об остатке от деления первого числа на второе в следующем формате:
#
# Остаток от деления X
# Если он равен 0, то число A делится нацело на число B
# В указанном примере
# X - остаток от деления  A A на  B, где  A - первое введенное число, а  B - второе.

a = int(input())
b = int(input())

x = a % b

print(f"Остаток от деления {x}")
print(f"Если он равен 0, то число {a} делится нацело на число {b}")