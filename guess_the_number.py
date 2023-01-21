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
            return int(input('Guess the secret number? '))
        except:
            print('That is not a number')
            


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    guess_attempt = 0
    guess_count = 5
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        # guess counter
        guess_count = guess_count - 1
        guess_attempt = guess_attempt + 1
        if result == correct:
            print(f'It took you {guess_attempt} guesses.')
            break
        elif guess_count != 0:
            print(f'You have {guess_count} guesses left.')
        elif guess_count == 0:
            print('No more guesses')
            break

    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
