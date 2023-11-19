# Немного измените код прошлой задачи (class_beginner_1.6.2): допишите код, который выводит результат деления исходного числа на полученное число (то есть исходное число, записанное наоборот). Результат данного деления округлите до 6 знаков после запятой.

number = input()
digits = list(map(int, str(number)))
rev_digits = int(''.join(map(str, reversed(digits))))

result_string = ''.join(map(str, reversed(digits)))
splitted_string = ' '.join(map(str, result_string))

print(splitted_string)
print(result_string)

result_division = round(int(number) / rev_digits, 6)
print(f"{number} / {rev_digits} = {result_division}")