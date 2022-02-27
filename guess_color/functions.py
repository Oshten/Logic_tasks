import random


class Item:
    """Класс объект"""
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color


def make_item(color):
    """Создание одного предмета"""
    return Item(color=color)


def make_items():
    """Создение 100 предметов"""
    quentity_items = 100
    quentity_blue_items = random.randint(60, 65)
    quentity_red_items = quentity_blue_items // 2
    quentity_green_items = quentity_items - quentity_blue_items - quentity_red_items
    list_items = []
    items = []
    for _ in range(quentity_blue_items):
        list_items.append(make_item('blue'))
    for _ in range(quentity_red_items):
        list_items.append(make_item('red'))
    for _ in range(quentity_green_items):
        list_items.append(make_item('green'))
    while list_items:
        if len(list_items) > 1:
            index = random.randint(0, len(list_items)-1)
            item = list_items.pop(index)
        else:
            item = list_items.pop()
        items.append(item)
    return items

