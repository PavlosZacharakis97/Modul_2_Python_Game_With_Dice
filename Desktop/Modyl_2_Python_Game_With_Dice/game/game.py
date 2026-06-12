import random
from datetime import datetime
from game.models import Player, Computer
from game.settings import GAME_LEVELS, GAME_LEVELS_CONVERT
from game.exceptions import InvalidInputError
from game.score import save_result

def start_game():
    print("\n=== Игра Кости ===")
    
    name = input("Введите ваше имя: ").strip()
    if not name:
        raise InvalidInputError("Имя не может быть пустым!")
    
    print("\nВыберите уровень:")
    print("1 - Short  (5 раундов)")
    print("2 - Medium (8 раундов)")
    print("3 - Long   (10 раундов)")
    
    level = input("Ваш выбор: ").strip()
    if level not in GAME_LEVELS:
        raise InvalidInputError("Неверный уровень! Введите 1, 2 или 3")
    
    rounds = GAME_LEVELS[level]
    player = Player(name)
    computer = Computer()


    print(f"\nИгра началась! Уровень: {GAME_LEVELS_CONVERT[rounds]}, Раундов: {rounds}")
    start_time = datetime.now()

    for round_num in range(1, rounds + 1):
        print(f"\n--- Раунд {round_num} ---")
        
        while True:
            user_input = input("Нажмите Enter чтобы бросить кубик: ")
            if user_input == "":
                break
            print('Бросок не сделан!!! Нажмите "Enter" для повторного броска.')
        
        player_roll = player.roll_dice()
        computer_roll = computer.roll_dice()
        
        print(f"Вы бросили кубик: {player_roll}")
        print(f"Компьютер бросил кубик: {computer_roll}")
        
        if player_roll == computer_roll:
            print("Ничья! Перебрасываем кубики...")
            continue
        
        difference = player_roll - computer_roll
        
        if player_roll > computer_roll:
            print(f"Разница: +{difference} очка")
        else:
            print(f"Разница: {difference} очков")
        
        player.update_score(difference)
        print(f"Текущий счет: {player.score}")



    print("\n=== Итоги игры ===")
    print(f"Время начала: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Игрок: {player.name}")
    print(f"Уровень: {GAME_LEVELS_CONVERT[rounds]}")
    print(f"Итоговый счет: {player.score}")
    
    if player.score > 0:
        print("Вы победили!")
    elif player.score < 0:
        print("Победил компьютер,а ты приёмный!")
    else:
        print("Ничья не принимается. Ебашим до конца")
    
    save_result(player.name, rounds, player.score)
    print("\nРезультат сохранён!")