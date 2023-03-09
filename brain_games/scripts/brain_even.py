import random
from brain_games.cli import welcome_user


def is_even(num):
    return num % 2 == 0


def main():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    correct_answers = 0
    while correct_answers < 3:
        num = random.randint(1, 100)
        print(f"Question: {num}")
        user_answer = input("Your answer: ")
        if (is_even(num) and user_answer == "yes") or (
                not is_even(num) and user_answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct \
answer was '{'yes' if is_even(num) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
