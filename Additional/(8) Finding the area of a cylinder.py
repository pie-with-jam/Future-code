radius = float(input("Введите радиус цилиндра: "))
height = float(input("Введите высоту цилиндра: "))

base_area = 3.14 * radius ** 2
lateral_area = 2 * 3.14 * radius * height

total_area = 2 * base_area + lateral_area

print("Площадь поверхности цилиндра:", total_area)