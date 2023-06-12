#!/usr/bin/env python3


import prompt
from random import randint
import random


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def welcome_user():
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    return name


def calc(name):
    print('What is the result of the expression?')
    item = 0
    math_list = ["+", "-", "*"]
    while item < 3:
        number1 = randint(10, 20)
        number2 = randint(1, 10)
        math = random.choice(math_list)
        print(f'Question: {number1} {math} {number2}')
        join = prompt.string('Your answer: ')
        if math == "+":
            result = number1 + number2
        elif math == "-":
            result = number1 - number2
        elif math == "*":
            result = number1 * number2
        if result == int(join):
            item += 1
            print('Correct!')
        else:
            item = 4
            print(f"'{join}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {name}!")
        if item == 3:
            print(f'Congratulation, {name}!')


if __name__ == '__main__':
    names = main()
    calc(names)
