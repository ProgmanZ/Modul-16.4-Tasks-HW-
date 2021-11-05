# Задача 7. Ролики

def enter_list(ask_arg_one, ask_arg_two, number):
    ent_list = []
    for n in range(number):
        print(ask_arg_one, n + 1, ask_arg_two, end='')
        ent_list.append(int(input()))
    return ent_list


def search_size(size_skates_list, size_legs_list):
    count = 0
    for size_leg in size_legs_list:
        while True:
            if size_leg in size_skates_list:
                count += 1
                size_skates_list.remove(size_leg)
                break

            else:
                if len(size_skates_list) == 0:
                    print("Коньков меньше чем людей!")
                    break
                elif size_leg <= max(size_skates_list):
                    size_leg += 1
                else:
                    break
    return count


ask = ['Размер', 'пары :', 'Размер ноги', 'человека :']

n = int(input("Кол-во коньков: "))
n = enter_list(ask[0], ask[1], n)

k = int(input("\nКол-во людей: "))
k = enter_list(ask[2], ask[3], k)

cnt = search_size(n, k)

print("\nНаибольшее кол-во людей, которые могут взять ролики:", cnt)
