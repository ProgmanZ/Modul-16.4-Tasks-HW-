# Задача 5. Песни

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

quantity = int(input('Сколько песен выбрать? '))
count = 0

for i in range(quantity):
    song = input(f'Название {i + 1} песни: ')
    for song_name in violator_songs:
        if song == song_name[0]:
            count += song_name[1]

print(f'\nОбщее время звучания песен: {round(count,2)} минут.')
