"""Function that greet user and return it's name"""
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name
