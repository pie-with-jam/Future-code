# Вася с папой решили съездить на дачу. Папа поручил Васе рассчитать стоимость поездки на автомобиле (туда и обратно). Исходными данными являются: расстояние до дачи (в километрах); количество бензина, которое потребляет автомобиль на 100 км пробега; цена одного литра бензина (в руб.).

distance = float(input())
fuel_consumption = float(input())
fuel_price = float(input())

total_fuel = (distance * 2 / 100) * fuel_consumption

trip_cost = total_fuel * fuel_price

print(round(trip_cost, 3))