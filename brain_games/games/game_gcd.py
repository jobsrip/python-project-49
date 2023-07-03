from random import randint
from math import gcd


MIN_NUM = 1
MAX_NUM = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question_and_correct_answer():
    """Make question and generate correct answer for the game."""
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    correct_answer = gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(correct_answer)
