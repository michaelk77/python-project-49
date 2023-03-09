import random
from brain_games.scripts.logic import play_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_question():
    question = random.randint(1, 100)
    correct_answer = "yes" if is_prime(question) else "no"
    return str(question), correct_answer


def main():
    play_game(generate_question,
              "Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


if __name__ == '__main__':
    main()
