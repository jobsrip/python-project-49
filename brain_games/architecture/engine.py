#!/usr/bin/env python3
import prompt
from random import randint

def loose(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer. ;(. Correct answer was {correct_answer}.)")
    print(f"Let's try again, {name}!")
    

def win(name):
    print(f"Congratulations, {name}!")
    
    

def my_function():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name



    
def check(answer, correct_answer, score, score_to_win):    
    if answer == correct_answer:
        score +=1 
        print('Correct!')

    if answer != correct_answer:
        loose()
    
    if score == score_to_win:
        win()
        

def even_question():
        a = randint(1,100)
        print(f"Answer 'yes' if the nubmer is even. Otherwise answer 'no'.")
        print(f"Question: {a}")
        answer = input("Your answer: ")
        correct_answer = ''
        if a % 2 == 0: 
                correct_answer = 'yes'
        else:
                correct_answer = 'no'
        
        return answer, correct_answer

        
        






if __name__ == '__main__':
    my_function()
    

    