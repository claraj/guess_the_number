import random

print('Guess the Number Game')

correct = 'you guessed correctly!'

too_low = 'Too Low!!'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    try: 
        return int(input('Guess the secret number? '))
    except:
        print("Please enter numbers only")
         
    
 
   
    
   


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
        counter = counter+1
        print(result)

        if result == correct:
            break

    print(f'Thanks for playing the game! You guessed {counter} times.')


if __name__ == '__main__':
    main()
