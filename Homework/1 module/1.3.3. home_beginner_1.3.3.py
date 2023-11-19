import math

radius = int(input())

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
volume = (4/3) * math.pi * radius ** 3
surface_area = 4 * math.pi * radius ** 2

print(f"Длина окружности радиуса {radius} равна {round(circumference, 3)}")
print(f"Площадь круга радиуса {radius} равна {round(area, 3)}")
print(f"Объем шара радиуса {radius} равен {round(volume, 3)}")
print(f"Площадь поверхности шара радиуса {radius} равна {round(surface_area, 3)}")