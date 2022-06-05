"""command line utils."""


import prompt


def welcome_user():
    """Prompt user name and welcome."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
