"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    while True:
        count += 1
        if number > predict:
           while number > predict:
               predict += predict/2
           if number < predict:
                while number < predict:
                    predict -= 1
             
        elif number < predict:
            while number < predict:
                predict -= predict/2
            if number > predict:
                while number > predict:
                    predict += 1
                
        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break #конец игры выход из цикла
    return count

game_core_v3()