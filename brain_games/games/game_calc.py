from random import choice, randint
from operator import sub, add, mul

MIN_NUMBER = 1
MAX_NUMBER = 10
DESCRIPTION = 'What is the result of the expression?'


def make_question_and_correct_answer():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operation, operator = choice([
        (add, '+'),
        (mul, '*'),
        (sub, '-'),
    ])

    correct_answer = operation(num1, num2)
    question = f"{num1}{operator}{num2}"
    return question, str(correct_answer)