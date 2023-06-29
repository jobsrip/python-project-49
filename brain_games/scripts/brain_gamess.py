#!/usr/bin/env python3
import prompt



def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Welcome to the Brain Games!')
   

if __name__ == '__main__':
    main()
