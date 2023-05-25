"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

"""Сначала устанавливаем любое random число, а потом уменьшаем
или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток
       
Args:
    number (int, optional): Загаданное число. Defaults to 1.

Returns:
    int: Число попыток
"""

number = np.random.randint(1, 101)

count = 1
predict = 50
    
while True:
    if number > predict:
        while number > predict:
            count += 1
            difference = (100 - predict)//2
            predict += difference
        if number < predict:
            while number < predict:
                count += 1
                predict -= 1
             
    elif number < predict:
        while number < predict:
            count += 1
            predict -= predict//2
        if number > predict:
            while number > predict:
                count += 1
                predict += 1
                
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла    