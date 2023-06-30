#!/usr/bin/env python3


from brain_games.architecture.engine import loose, win, my_function, check, even_question




def main():
    
    score = 0
    score_to_win = 3
    my_function()
    while score < score_to_win:
        even_question()
        check(answer, correct_answer, score, score_to_win)

main()















if __name__ == '__main__':
    main()
