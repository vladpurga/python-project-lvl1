"""even game."""


import random

import prompt


def welcome_user():
    """Prompt user name and welcome.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def print_warning(name, answer, correct):
    """Print warning message.

    Args:
        name: user name
        answer: user' wrong answer
        correct: right answer
    """
    warning = "'{wrong}' is wrong answer ;(. Correct answer was '{right}'."
    print(warning.format(wrong=answer, right=correct))
    print("Let's try again, {0}!".format(name))


def game():
    """even-game engine."""
    count_steps = 3

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(count_steps):
        guess = random.randint(1, 100)  # noqa: S311
        is_even = guess % 2 == 0

        print('Question: {0}!'.format(guess))
        answer = prompt.string('Your answer: ')

        if is_even:
            if answer == 'yes':
                print('Correct!')
            else:
                print_warning(name, answer, 'yes')
                return
        else:
            if answer == 'no':
                print('Correct!')
            else:
                print_warning(name, answer, 'no')
                return

    print('Congratulations, {0}!'.format(name))
