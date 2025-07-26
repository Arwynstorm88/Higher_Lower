import random

#prompt for Upper and Lower Bounds
upper_bound = int(input("Enter upper bound: "))
lower_bound = int(input("Enter lower bound: "))

#validate that the lower bound is lower than the upper bound
while lower_bound >= upper_bound:
    print('Lower bound should be LOWER than upper bound.')
    lower_bound = int(input("Enter lower bound: "))

#set a random number within the bounds
number = random.randint(lower_bound, upper_bound)

#prompt the user for a guess
user_guess = int(input('Great, now guess a number between {} and {} '.format(lower_bound, upper_bound)))

number_guesses = 0 #set number of guesses to 0
#initialize game loop, checks if guess is within the bound and if it matches the number
while user_guess != number:
    if user_guess < lower_bound or user_guess  > upper_bound:
        print('Invalid guess, guess must be between {} and {}'.format(lower_bound, upper_bound))
    elif user_guess > number:
        number_guesses += 1
        print('Nope, too high.')
    elif user_guess < number:
        number_guesses += 1
        print('Nope, too low.')

    user_guess = int(input('Guess another number: '))

#prints winning statement and total guesses
print('You got it! \nYour total guesses were {}'.format(number_guesses))
