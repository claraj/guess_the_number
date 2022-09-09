""" 1- Once the user has guessed correctly, display the number of guesses it took

Hint: add a counter variable in the main function and increment it when the while loop repeats. 

    2- Handle ValueError if user enters input other than an integer.
    https://github.com/claraj/ProgrammingLogic1150Examples/blob/c874241cb507ee3d84c8506de69ce106134f45b5/4_loops/while_loop_check_for_number.py#L47-L60 """

import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    while True:
        try:
            user_entry = int(input('Guess the secret number? '))
            return user_entry
        except ValueError:
            print('Please enter a valid number')


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    counter = 0
    
    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        counter = counter + 1
        print(result)

        if result == correct:
            break

    print('It took you ' + str(int(counter)) + ' guesses.')
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
