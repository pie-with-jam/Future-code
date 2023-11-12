# Напишите программу, которая вводит наименование продукта, цену, вес (количество), рассчитывает стоимость и выводит чек (см. пример ввода-вывода, в точности повторите чек):

first_product = input()
first_product_price = float(input())
first_product_weight = float(input())
second_product = input()
second_product_price = float(input())
second_product_weight = float(input())
first_product_total_price = first_product_price * first_product_weight
second_product_total_price = second_product_price * second_product_weight

param_1 = "20"
param_2 = "7"
param_3 = "8"
param_4 = "9"

col_1 = "Наименование изделия"
col_2 = "Цена"
col_3 = "Вес/Кол."
col_4 = "ВСЕГО"
s = "-"
itog = "ИТОГО"

print(col_1.center(20), col_2.center(7), col_3.center(8), col_4.center(9))
separ = s * int(param_1) + " " + s * int(param_2) + " " + s * int(param_3) + " " + s * int(param_4)
print(separ)
print(format(first_product, param_1), format(first_product_price, param_2 + ".2f"),
format(first_product_weight, param_3 + ".2f"), format(first_product_total_price, param_4 + ".2f"))
print(format(second_product, param_1), format(second_product_price, param_2 + ".2f"),
format(second_product_weight, param_3 + ".2f"), format(second_product_total_price, param_4 + ".2f"))
print(separ)
print(format(itog, str(int(param_1) + int(param_2) + int(param_3) + 2)),
format(first_product_total_price + second_product_total_price, param_4 + ".2f"))