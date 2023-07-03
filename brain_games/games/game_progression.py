from random import randint

START_MIN, START_MAX = 1, 50
STEP_MIN, STEP_MAX = 2, 5
LENGTH_MIN, LENGTH_MAX = 5, 10
DESCRIPTION = 'What number is missing in the progression?'


def make_progression(start, step, length):
    """Generate a random progression with a random step and length"""

    progression = [str(start + i * step) for i in range(length)]
    return progression


def hide_element(progression):
    """Hide random element"""

    secret_index = randint(0, len(progression)-1)
    secret_element = progression[secret_index]
    progression[secret_index] = '..'
    return secret_element, progression


def make_question_and_correct_answer():
    """Make question and generate correct answer for the game."""

    start = randint(START_MIN, START_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    length = randint(LENGTH_MIN, LENGTH_MAX)
    progression = make_progression(start, step, length)
    correct_answer, progression = hide_element(progression)
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
