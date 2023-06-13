import prompt
from random import randint


def game_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    item = 0
    while item < 3:
        num1 = randint(1, 10)
        num2 = randint(100, 120)
        num_prog = randint(1, 8)
        numbers = []
        for i in range(num1, num2, num_prog):
            numbers.append(i)
        number1 = randint(0, 9)
        number2 = numbers[number1]
        numbers[number1] = '..'
        list_numbers = " ".join(map(str, numbers[0:10]))
        print(f'Question: {list_numbers}')
        join = prompt.integer('Your answer: ')
        if join == number2:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(
                f"'{join}' is wrong answer ;(. "
                f"Correct answer was '{number2}'\nLet's "
                f"try again, {name}!")
        if item == 3:
            print(f'Congratulations, {name}!')
