#!/usr/bin/env python3


import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def welcome_user():
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    return name


def even(name):
    print('Answe "yes" if the number is even, otherwise answer "no".')
    item = 0
    while item < 3:
        number = randint(1, 9999999)
        print(f'Question: {number}')
        join = prompt.string('Your answer: ')
        if (number % 2 == 0 and join.lower() == 'yes') or (number % 2 == 1 and join.lower() == 'no'):
            item += 1
            print('Correct!')
        elif (join.lower() == 'yes'):
            item = 4
            print(f"'{join}' is wrong answer ;(. Correct answer was 'no'\nLet's try again, {name}!")
        elif (join.lower() == 'no'):
            item = 4
            print(f"'{join}' is wrong answer ;(. Correct answer was 'yes'\nLet's try again, {name}!")
        if item == 3:
            print(f'Congratulation, {name}!')


if __name__ == '__main__':
    names = main()
    even(names)
