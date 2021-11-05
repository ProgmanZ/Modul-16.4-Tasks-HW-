# Задача 3. Детали

def f_list(search_part, db_list):
    # Функция создает временный список из нулевых элементов входящего - основного списка db_shop.
    # Возвращает количество искомых запчастей, сумму стоимости этих запчастей
    temp_list = []
    count_part = 0
    cost = 0

    for cell in db_list:
        temp_list.append(cell[0])
    count_part = temp_list.count(search_part)

    for element in db_list:
        if search_part == element[0]:
            cost += element[1]

    return count_part, cost


shop = [['каретка', 1200],
        ['шатун', 1000],
        ['седло', 300],
        ['педаль', 100],
        ['седло', 1500],
        ['рама', 12000],
        ['обод', 2000],
        ['шатун', 200],
        ['седло', 2700]
        ]

part = input("Название детали: ")

count, all_cost = f_list(part, shop)

print("Кол-во деталей -", count)
print("Общая стоимость -", all_cost)
