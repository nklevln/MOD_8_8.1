"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

number = np.random.randint(1, 101)

# Изачально предполагаем середину интервала [1: 101], равную 50, это наша первая попытка.
count = 1
predict = 50
    
while True:
    # Если предполагаемое число меньше загаданного, сокращаем интервал с шагом 1/2, пока не "перешагнем" его.
    if number > predict:
        while number > predict:
            count += 1
            difference = (100-predict) // 2
            predict += difference
        # Как только перешагнули, идем обратно с шагом 1
        if number < predict:
            while number < predict:
                count += 1
                predict -= 1
    
    # Логика, обратная предыдущему пункту, для случая, когда загаданное меньше предполагаемого.         
    elif number < predict:
        while number < predict:
            count += 1
            predict -= predict // 2
        if number > predict:
            while number > predict:
                count += 1
                predict += 1
    
    # Нашли число, вышли из цикла с указанием затраченных попыток.            
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break   