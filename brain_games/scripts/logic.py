from brain_games.scripts.cli import welcome_user


def play_game(generate_question, GAME_DESCRIPTION):
    """Запускает игру"""
    name = welcome_user()
    print(GAME_DESCRIPTION)
    correct_answers_count = 0
    while correct_answers_count < 3:
        question, correct_answer = generate_question()
        user_answer = input(f"Question: {question}\nYour answer: ")
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(\
. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            correct_answers_count += 1
    print(f"Congratulations, {name}!")
