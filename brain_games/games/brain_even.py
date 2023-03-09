import random
from brain_games.scripts.logic import play_game


def generate_question():
    number = random.randint(1, 100)
    if number % 2 == 0:
        return number, "yes"
    else:
        return number, "no"


def main():
    play_game(generate_question,
              "Answer \"yes\" if the number is even, otherwise answer \"no\".")


if __name__ == '__main__':
    main()
