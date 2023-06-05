#!/usr/bin/env python3

from random import randint
from brain_games.scripts.brain_games import main


def brain_even():

    brain_games.scripts.brain_games.main()


    counter = 0
    while counter < 3:

        a = randint(1, 100)

        print(f"Answer 'yes' if the number is even. Otherwise answer 'no'.")
        print(f"Question: {a}")
        answer = input("Your answer: ")

        if a % 2 == 0 and answer == 'yes' or a % 2 != 0 and answer == 'no':
            counter = counter + 1
            print('Correct!')

        if a % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer. ;(. Correct answer was 'yes'")
            print(f"Let's try again, Bill!" )
            break

        if a % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer. ;(. Correct answer was 'no'")
            print(f"Let's try again, Bill!")
            break

        if counter == 3:
            print (f"Congratulations, Bill!")


if __name__ == '__main__':
    main()
