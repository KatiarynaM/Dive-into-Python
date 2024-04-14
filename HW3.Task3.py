"""Создайте словарь со списком вещей для похода в качестве ключа и их массой 
в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.*Верните все возможные
варианты комплектации рюкзака."""

def pack_backpack(items, max_weight):
    things = []
    for item, weight in items.items():
        if weight <= max_weight:
            things.append(item)
            max_weight -= weight
    return things

items = {'еда': 3, 'вода': 4, 'полатка': 2, 'зонт': 1, 'топор': 1, 'кровать':7, 'спальный мешок':1,}
max_weight = 10
print(pack_backpack(items, max_weight)) 