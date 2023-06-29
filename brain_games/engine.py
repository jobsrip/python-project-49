#!/usr/bin/env python3
import prompt


def my_function():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


    