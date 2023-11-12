# Напишите программу, которая считывает часы и минуты (именно в таком порядке) и выводит, сколько минут уже прошло с полуночи и сколько осталось до полуночи. Формат вывода должен быть следующий:
#
# Прошло N минут, осталось M минут

hours = int(input())
minutes = int(input())

minutes_since_midnight = hours * 60 + minutes

minutes_until_midnight = 24 * 60 - minutes_since_midnight

print(f"Прошло {minutes_since_midnight} минут, осталось {minutes_until_midnight} минут")
