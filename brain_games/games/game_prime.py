from random import randint

MIN_NUM = 2
MAX_NUM = 100

DESCRIPTION =f"Answer 'yes' if the given number is prime. Otherwise answer 'no'."




def is_prime(num: int) -> bool:   # Checking if the nubmer is prime
                                  
    flag = True
    
    for i in range(2, num):
       
        if num % i == 0:
            flag = False
            return flag 
    
    return flag

        

        
    


def make_question_and_correct_answer(): # make question and answer for the game
    
    num = randint(MIN_NUM, MAX_NUM)
    question = str(num)
    
    
    if is_prime(num):
        correct_answer = 'yes'
    
    else: 
        correct_answer = 'no'

    
    return str(question), str(correct_answer    )



        