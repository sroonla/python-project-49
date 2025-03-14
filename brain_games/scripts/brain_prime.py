import random

from brain_games.engine import run_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct_answer


def main():
    run_game(RULES, generate_round)


if __name__ == "__main__":
    main()
