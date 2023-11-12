# Напишите программу, которая считывает год рождения человека и выводит на экран, сколько человеку исполнится лет в этом году в следующем формате:
#
# В этом году вам исполнится N года (лет)

from datetime import datetime

Year_of_birth = int(input())
age = currentYear = datetime.now().year - Year_of_birth
print(f"В этом году вам исполнится {age} года (лет)")