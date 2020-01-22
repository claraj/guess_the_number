import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    count = 0

    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        count += 1
        return correct
    if guess < secret:
        count += 1
        return too_low
        count += 1
    if guess > secret:
        count += 1
        return too_high


def main():
    (low, high) = configure_range()
    secret = generate_secret(low, high)


    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break


if __name__ == '__main__':
    main()
