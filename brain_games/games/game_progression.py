from random import randint, choice

START_NUMBER = 1
END_NUMBER = 50
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 2
MAX_STEP = 5 
DESCRIPTION = 'What number is missing in the progression?'



def make_progression(start, end, step):

    start = randint(START_NUMBER, END_NUMBER)
    step = randint(MIN_STEP, MAX_STEP) 
    length = randint(MIN_LENGTH, MAX_LENGTH) 
    end = (start + (step * (length - 1)))
    range_in_list = [str(start + i * step) for i in range (length)]
    progression = ''.join(range_in_list)
    return progression






def make_question_and_correct_answer():
    
    
