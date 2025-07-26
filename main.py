import random

def play_game(high_score):
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
    if high_score is None or number_guesses < high_score:
        high_score = number_guesses
        print('NEW HIGH SCORE!')
    print('Your current high score is {}'.format(high_score))


    play_again = input('Would you like to play again? (yes/no): ').lower()
    while play_again not in ['yes', 'no']:
       play_again = input('Invalid input. Would you like to play again? (yes/no): ').lower()
    if play_again == 'yes':
        return play_game(high_score)
    else:
        print('Thank you for playing!')
        return high_score

high_score = None
high_score = play_game(high_score)