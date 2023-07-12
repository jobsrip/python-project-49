from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 999


def is_even(num: int) -> bool:
    """Check if the nubmer is even or not"""
    flag = False
    if num % 2 == 0:
        flag = True
    return flag


def make_question_and_correct_answer():
    """Make question and generate correct answer for the game"""
    num = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(num)

    if is_even(num):
        correct_answer = 'yes'

    else:
        correct_answer = 'no'
        return question, correct_answer
