# Задача 6. Уникальные элементы

def enter_list(number):
    ent_list = []
    for n in range(number):
        ent_list.append(int(input(f"Введите {n + 1} число из {number}: ")))
    return ent_list


def set_list(unique_list):
    for n in unique_list:
        while unique_list.count(n) != 1:
            unique_list.remove(n)
    return unique_list


print("Ввод первого списка:")
list_a = enter_list(3)

print("\nВвод второго списка:")
list_b = enter_list(5)

print("Первый список: ", list_a)
print("Второй список: ", list_b)

list_a.extend(list_b)
list_a = set_list(list_a)

print("Новый первый список с уникальными элементами: ", list_a)
# решение может быть короче с set, но не стал применять т.к. не проходили