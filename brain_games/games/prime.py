import prompt
from random import randint


def its_prime(num):
    k = 0
    for i in range(2, num // 2+1):
        if num % i == 0:
            k += 1
    if k == 0:
        return 'yes'
    else:
        return 'no'


def game_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    item = 0
    while item < 3:
        number1 = randint(1, 50)
        prime = its_prime(number1)
        print(f'Question: {number1}')
        join = prompt.string('Your answer: ')
        if join.lower() == prime:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(
                f"'{join}' is wrong answer ;(. "
                f"Correct answer was '{prime}'\nLet's "
                f"try again, {name}!"
                )
        if item == 3:
            print(f'Congratulations, {name}!')
