import random
from brain_games.scripts.logic import play_game

OPERATORS = ('+', '-', '*')
GAME_DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(OPERATORS)
    question = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, str(answer)


def main():
    play_game(generate_question, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
