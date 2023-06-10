#!/usr/bin/env python3


import prompt
from random import randint
import random
import math


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def welcome_user():
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    return name


def NOD(name):
    print('Find the greatest common divisor of given numbers.')
    item = 0
    while item < 3:
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        print(f'Question: {number1} {number2}')
        join = prompt.integer('Your answer: ')
        g_c_d = math.gcd(number1, number2)
        if join == g_c_d:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(f"'{join}' is wrong answer ;(. Correct answer was '{g_c_d}'\nLet's try again, {name}!")
        if item == 3:
            print(f'Congratulation, {name}!')


if __name__ == '__main__':
    names = main()
    NOD(names)
