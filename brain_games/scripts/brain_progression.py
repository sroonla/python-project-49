import random

from brain_games.engine import run_game

RULES = "What number is missing in the progression?"


def generate_round():
    start = random.randint(1, 20)  # Начало
    step = random.randint(2, 5)  # Шаг
    length = random.randint(5, 10)  # Длина (от 5 до 10)

    progression = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer


def main():
    run_game(RULES, generate_round)


if __name__ == "__main__":
    main()
