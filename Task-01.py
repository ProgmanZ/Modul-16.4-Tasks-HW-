# Задача 1. Страшный код

def delete_num(number, from_list):
    while from_list.count(number):
        from_list.remove(number)
    return from_list


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_five = a.count(5)
a = delete_num(5, a)
a.extend(c)
count_three = a.count(3)

print("Результат работы программы:")
print("Кол-во цифр 5 при первом объединении:", count_five)
print("Кол-во цифр 3 при втором объединении:", count_three)
print("Итоговый список:", a)
