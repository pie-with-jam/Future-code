# В школе у Степана решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них. Каждый класс сидит в своем кабинете.

class1_students = int(input())
class2_students = int(input())
class3_students = int(input())

class1_desks = class1_students // 2 + class1_students % 2
class2_desks = class2_students // 2 + class2_students % 2
class3_desks = class3_students // 2 + class3_students % 2

total_desks = class1_desks + class2_desks + class3_desks

print(total_desks)