# Используя арифметические операции со строками (конкатенацию), "нарисуйте" в консоли следующую фигуру:
#
# *********************
# *   *   *   *   *   *
# *   *   *   *   *   *
# *********************
# *   *   *   *   *   *
# *   *   *   *   *   *
# *********************
# *   *   *   *   *   *
# *   *   *   *   *   *
# *********************
# *   *   *   *   *   *
# *   *   *   *   *   *
# *********************

i = 0
while i <= 3:
    print("*" * 21)
    for a in range(0, 2):
        print("*", "*", "*", "*", "*", "*", sep="   ")
    i = i + 1
print("*" * 21)