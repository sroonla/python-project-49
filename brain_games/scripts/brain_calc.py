import operator
import random

from brain_games.engine import run_game

RULES = "What is the result of the expression?"


def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation, func = random.choice([
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    ])
    question = f"{num1} {operation} {num2}"
    correct_answer = str(func(num1, num2))
    return question, correct_answer


def main():
    run_game(RULES, generate_round)


if __name__ == "__main__":
    main()