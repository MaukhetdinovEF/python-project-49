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


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    item = 0
    while item < 3:
        number1 = randint(1, 50)
        k = 0
        for i in range(2, number1 // 2+1):
            if number1 % i == 0:
                k += 1
        if k == 0:
            unswer = 'yes'
        else:
            unswer = 'no'
        print(f'Question: {number1}')
        join = prompt.string('Your answer: ')
        if join.lower() == unswer:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(f"'{join}' is wrong answer ;(. Correct answer was '{unswer}'\nLet's try again, {name}!")
        if item == 3:
            print(f'Congratulation, {name}!')


if __name__ == '__main__':
    names = main()
    prime(names)
