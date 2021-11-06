# Задача 8. Считалка


def del_position(step, start_position, list_people):
    ppl = len(list_people)
    while start_position <= ppl and step != 0:
        start_position += 1
        step -= 1
        if start_position == ppl:
            start_position = 0
    return start_position


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
    start = del_part + 1
    count_peoples = len(participants)

print("Остался человек под номером", participants[0])
