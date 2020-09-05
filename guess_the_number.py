import random

correct = 'You guessed correctly!'
too_low = 'Too Low'
too_high = 'Too High'

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 1000


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    try:
        return int(input('Guess the secret number? '))
    except ValueError as e:
        print("Please enter a number.")
    

def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high




def main():
    rerun = True
    while rerun:
        (low, high) = configure_range()
        secret = generate_secret(low, high)
        counter = 0
        while True:
            guess = get_guess()
            counter +=1
            result = check_guess(guess, secret)
            print(result)

            if result == correct:
                print(f'You took {counter} guesses')
                rerun_string = input('Would you like to play again? Enter Y to play again  ')
                if rerun_string.lower() != 'y':
                    rerun = False
                    
                break
        

if __name__ == '__main__':
    main()
