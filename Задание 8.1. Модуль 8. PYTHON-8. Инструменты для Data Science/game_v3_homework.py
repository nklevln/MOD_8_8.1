"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

number = np.random.randint(1, 101)

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    #predict = np.random.randint(1, 101)
    predict = 50
    
    while number != predict:
        count += 1
        if number > predict:
            while number > predict:
                predict += predict/2
            if number < predict:
                predict -= 1
             
        elif number < predict:
            while number > predict:
                predict -= predict/2
            if number > predict:
                predict += 1
                
        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break #конец игры выход из цикла
        
        #return count
    
    
game_core_v3(number)