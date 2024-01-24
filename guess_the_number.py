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

def increment_guess_counter(total_guesses):
    """Increments the total guesses for each successive loop"""
    total_guesses += 1
    return total_guesses

def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    total_guesses = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        total_guesses = increment_guess_counter(total_guesses)
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print(f"It took you {total_guesses} guesses this time.")
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
