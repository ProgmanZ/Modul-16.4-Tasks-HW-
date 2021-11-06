# Задача 9. Друзья

def create_db_func(all_friends):
    list_db = []
    for i in range(all_friends):
        list_db.append([i + 1, 0])
    return list_db


def mutual_func(for_f, from_f, how_m, db_scr):
    db_scr[for_f][1] -= how_m
    db_scr[from_f][1] += how_m
    return db_scr


def print_db(db_list):
    for line in db_list:
        print(f'{line[0]} : {line[1]}')


friends = int(input("Кол-во друзей: "))
scrips = int(input("Долговых расписок: "))
scrips_db = create_db_func(friends)

for scrip in range(1, scrips + 1):
    print(f'\n{scrip} расписка')
    for_friend = int(input("Кому: ")) - 1
    from_friend = int(input("От кого: ")) - 1
    how_match = int(input("Сколько: "))
    scrips_db = mutual_func(for_friend, from_friend, how_match, scrips_db)

print("Баланс друзей:")
print_db(scrips_db)
