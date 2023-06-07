#!/usr/bin/env python3

import prompt
import random



def main():
    
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    
    score_to_win = 3
    score = 0
    
    while score < score_to_win:
    
    
        operator = random.choice(['+', '*', '-'])
        num1 = random.randint(5, 10)
        num2 = random.randint(1, 5)
        action  = f'{num1} {operator} {num2}'
        
        print('What is the result of the expression?')
        print(f"Question: {action}")
        answer = input('Your answer: ')
        correct_answer = ''
        
        if operator == '+':
            correct_answer = num1 + num2 
        
        if operator == '-':
            correct_answer = num1 - num2
        
        if operator == '*':
            correct_answer = num1 * num2

        correct_answer = str(correct_answer)
        
        if answer == correct_answer:
            score += 1
            print('Correct!')
        
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            break
        
        if score == score_to_win:
            print(f"Congratulations, {name}!")
            break



if __name__ == '__main__':
    main()
    
    