import json
import os
from datetime import datetime

RESULTS_FILE = "game_results.json"

def save_result(name, rounds, score):
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            results = json.load(f)
    else:
        results = []

    new_result = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Игрок": name,
        "Количество раундов": rounds,
        "Итоговый счет": score
    }

    results.append(new_result)

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def get_results():
    if not os.path.exists(RESULTS_FILE):
        print("Результатов пока нет!")
        return

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        results = json.load(f)

    for result in results:
        print(f"Дата: {result['Дата']}")
        print(f"Игрок: {result['Игрок']}")
        print(f"Количество раундов: {result['Количество раундов']}")
        print(f"Итоговый счет: {result['Итоговый счет']}")
        print("---------------------------------")