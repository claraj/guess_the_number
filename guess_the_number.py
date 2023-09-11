import random

correct = 'you guessed correctly!'
too_low = 'Too Low'
too_high = 'too high'



def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    try:
        return int(input('Guess the secret number? '))
    except:
        print('Please enter a numeral when guessing the secret number next time.')
        exit()



def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    user_guess_count = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        user_guess_count += 1
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print(f'You made {user_guess_count} guesses!')
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
