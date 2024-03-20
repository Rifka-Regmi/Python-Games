'''
This is a number guessing game in which random number is generated and the user needs to guess the number
'''
#Generates random number
import random
Num = random.randint(1, 10)
#The program runs until the user has guessed the correct answer
while True:
    Guess_num = int(input('Guess the number from 1 to 10: '))
    if Num == Guess_num:
        print('Correct')
        break
    elif Num < Guess_num:
        print('The number is smaller than the guessed number')
    else:
        print('The number is greater than the guessed number')