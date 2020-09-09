import random

correct = 'you guessed correctly!'
too_low = 'Too Low'
too_high = 'too high'
guess_count = 0

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    global guess_count
    '''get user's guess'''
    guess_count += 1
    return int(input('Guess the secret number? '))
    try:
        user_input = int(input('Guess the secret number? '))
    except ValueError as err:
        return f"{type(err)}: please enter a integer \"{err}\""
    return user_input



def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            print(f'It took you {guess_count} tries!')
            break


if __name__ == '__main__':
    main()
