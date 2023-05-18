# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Выбираем три случайные песни
random_songs = random.sample(my_favorite_songs, 3)

# Считаем общее время звучания выбранных песен
total_duration = sum(song[1] for song in random_songs)

# Выводим результат
print(f"Три песни звучат {total_duration:.2f} минут")

# Пункт B.
#  Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Выбираем три случайные песни
random_songs = random.sample(list(my_favorite_songs_dict.items()), 3)

# Считаем общее время звучания выбраных песен
total_duration = sum(song[1] for song in random_songs)

# Выводим результат
print(f"Три песни звучат {total_duration:,2f} минут")
