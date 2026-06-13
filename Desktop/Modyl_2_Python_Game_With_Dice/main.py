from game.game import start_game
from game.score import get_results
from game.exceptions import InvalidInputError

def main():
    while True:
        print("\n=== Главное меню ===")
        print("1 - Играть")
        print("2 - Посмотреть результаты")
        print("3 - Выйти")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            try:
                start_game()
            except InvalidInputError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            get_results()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Введите 1, 2 или 3")

if __name__ == "__main__":
    main()