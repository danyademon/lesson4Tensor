from prettytable import PrettyTable
colors = {'black': (0,0,0), 'red': (255,0,0)}

while True:
    print('0.Выход\n1.Добавить цвет\n2.Вывести все добавленные цвета')
    menu_selector = int(input())
    if (menu_selector < 0 
            or menu_selector > 2):
        #Ловит исключение, если такого пункта нет в меню
        print('Нет такого пункта в меню, попробуйте еще.')
        continue

    if menu_selector == 0:
        print('Удачи!')
        break
    elif menu_selector == 1:
        name = input('Введите название цвета: ')
        r =  int(input('Введите r: '))
        g =  int(input('Введите g: '))
        b =  int(input('Введите b: '))
        if ((r > 255) or
                (g > 255) or
                (b > 255) or 
                (r < 0) or 
                (g < 0) or 
                (b < 0)):
            print('Значение rgb лежит в диапазоне от 0 до 255. Попробуйте еще.')
            continue
        colors_in_dict = colors.keys()
        if name in colors_in_dict:
            print('Такой цвет уже есть в словаре')
        else: 
            colors.update({name: (r,g,b)})
    elif menu_selector == 2:
        for key,value in colors.items():
            print(f'Цвет: {key}\nRGB: {value}\n')