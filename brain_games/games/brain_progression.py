import random

from brain_games.scripts.logic import play_game


def generate_question():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    diff = random.randint(1, 5)
    hidden_index = random.randint(0, length - 1)
    progression = [start + i * diff for i in range(length)]
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(num) for num in progression)
    return question, correct_answer


def main():
    play_game(generate_question, "What number is missing in the progression?")


if __name__ == '__main__':
    main()
