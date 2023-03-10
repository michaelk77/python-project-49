import random
from brain_games.scripts.logic import play_game


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    return question, correct_answer


def main():
    play_game(generate_question,
              "Find the greatest common divisor of given numbers.")


if __name__ == '__main__':
    main()
