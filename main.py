import sys
import random

while True:
    try:
        number1 = int(input('give me first number: '))
        break
    except ValueError:
        print("It's not number")

while True:
    try:
        number2 = int(input('give me second number: '))
        break
    except ValueError:
        print("It's not number")


if number1 <= number2:
    number3 = random.randint(number1, number2)
else:
    number3 = random.randint(number2, number1)


while True:
    user_input = int(input('guess the number: '))
    if user_input == number3:
        print('bingo!')
        break
    else:
        print("You're wrong")
