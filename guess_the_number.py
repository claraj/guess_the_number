import random

correct = "you guessed correctly!"
too_low = "too low"
too_high = "too high"


def configure_range():
    """Set the high and low values for the random number"""
    return 1, 10


def generate_secret(low, high):
    """Generate a secret number for the user to guess"""
    return random.randint(low, high)


def get_guess():
    """get user's guess, as an integer number"""

    while True:
        # Use try and except clauses. Try to get users number and if it is not an integer, return again to get users input again
        try:
            # Moved users input to be stored in a variable instead.
            user_guess = int(input("Guess the secret number? "))

        except:
            # Catches the clause if it is anything else besides an integer. Prints a message to users terminal to prompt and enter a input
            print("Input a integer please.")

        else:
            # If everything checkouts, return the user number guess.
            return user_guess


def check_guess(guess, secret):
    """compare guess and secret, return string describing result of comparison"""
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
            break

    print("Thanks for playing the game!")


if __name__ == "__main__":
    main()
