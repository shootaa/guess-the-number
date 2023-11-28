import sys
import random

number1 = int(input('give me first number: '))
number2 = int(input('give me second number: '))

number3 = random.randint(number1, number2)

while True:
    user_input = int(input('guess the number: '))
    if user_input == number3:
        print('bingo!')
        break
    else:
        print("You're wrong")
