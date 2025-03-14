from brain_games.engine import run_game
import random

def get_question_and_answer():
    """Генерирует число и определяет, чётное оно или нет."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    
    return question, correct_answer

def main():
    """Запуск игры "Проверка на четность"."""
    run_game(get_question_and_answer)

if __name__ == "__main__":
    main()