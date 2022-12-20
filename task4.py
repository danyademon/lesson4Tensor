inventory = {}
max_weight = 1000.0
current_weight = 0.0

def add_item():
    """
    Добавление предмета в инвентарь
    """
    name = input('Введите название предмета: ')
    weight = input('Введите вес предмета: ')
    global current_weight
    if current_weight + float(weight) <= max_weight:
        items_in_inventory = inventory.keys()
        if (name in items_in_inventory):
            print('Такой предмет уже есть в инвентаре')
        else: 
            inventory.update({name: float(weight)})
            current_weight += float(weight)
    else: print('Недостаточно места в инвентаре')

def delete_item():
    """
    Удаление предмета из инвентаря
    """
    global current_weight
    name = input('Введите название предмета, который вы хотите удалить: ')

    if inventory.get(name, '1') == '1':
        print('Такого предмета нет в инвентаре')
    else:
        current_weight -= inventory[name]
        inventory.pop(name)

def show_items():
    """
    Вывод всех предметов в инвентаре
    """
    print(f'Общий вес: {current_weight}')
    for key,value in inventory.items():
        print(f'Название предмета: {key}\nВес предмета: {value}\n')

def show_items_sorted_by_weight_up():
    """
    Вывод всех предметов в инвентаре с сортировкой по весу от меньшего к большему
    """
    print(f'Общий вес: {current_weight}')
    inv_sorted = dict(sorted(inventory.items(), key=lambda value:value[1]))
    for key,value in inv_sorted.items():
        print(f'Название предмета: {key}\nВес предмета: {value}\n')

def show_items_sorted_by_weight_down():
    """
    Вывод всех предметов в инвентаре с сортировкой по весу от большего к меньшему
    """
    print(f'Общий вес: {current_weight}')
    inv_sorted = dict(sorted(inventory.items(), key=lambda value:value[1],reverse=True))
    for key,value in inv_sorted.items():
        print(f'Название предмета: {key}\nВес предмета: {value}\n')

while True:
    print('0.Выход\n1.Добавить предмет\n2.Удалить предмет\n3.Вывести список всех предметов\n4.Сортировка по весу по убывание\n5.Сортировка по весу по возрастание')
    menu_selector = int(input())
    if (menu_selector < 0
            or menu_selector > 5):
        print('Нет такого пункта в меню, попробуйте еще.')
        continue

    if menu_selector == 0:
        print('Удачи!')
        break
    elif menu_selector == 1:
        add_item()
    elif menu_selector == 2:
        delete_item()
    elif menu_selector == 3:
        show_items()
    elif menu_selector == 4:
        show_items_sorted_by_weight_down()
    elif menu_selector == 5:
        show_items_sorted_by_weight_up()

