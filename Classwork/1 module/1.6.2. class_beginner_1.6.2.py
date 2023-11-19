# Допишите к программе из предыдущей задачи (class_beginner_1.6.1) код, который создает из полученных цифр строку и выводит её и её тип данных (сначала строку, потом тип). Для определения типа данных используйте type.

number = input()
digits = list(map(int, str(number)))
rev_digits = reversed(digits)

result_string = ''.join(map(str, rev_digits))
splitted_string = ' '.join(map(str, result_string))

print(splitted_string)
print(result_string)
print(type(result_string))