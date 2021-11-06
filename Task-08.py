# Задача 8. Считалка


def del_position(step, position, list_people):
    quantity = len(list_people)
    while step != 1:
        position += 1
        step -= 1
        if position == quantity:
            position = 0
    return position


peoples = int(input("Кол-во человек: "))
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number} человек")

participants = list(range(1, peoples + 1))
count_peoples = len(participants)
start = 0

while count_peoples != 1:
    print("\nТекущий круг людей:", participants)
    print("Начало счёта с номера", participants[start])
    del_part = del_position(number, start, participants)
    print("Выбывает человек под номером", participants[del_part])
    participants.remove(participants[del_part])
    if del_part >= len(participants):
        start = 0
    else:
        start = del_part
    count_peoples = len(participants)

print("\nОстался человек под номером", participants[0])
