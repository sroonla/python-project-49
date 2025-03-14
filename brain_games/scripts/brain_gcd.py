from brain_games.engine import run_game
import random
import math

RULES = "Find the greatest common divisor of given numbers."

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer

def main():
    run_game(RULES, generate_round)

if __name__ == "__main__":
    main()