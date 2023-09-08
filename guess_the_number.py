import random


CORRECT = "you guessed correctly!"
TOO_LOW = "too low"
TOO_HIGH = "too high"


def configure_range():
    """Set the high and low values for the random number"""

    return 1, 1000  # Change range to be 1000 instead of 10.


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
        return CORRECT
    if guess < secret:
        return TOO_LOW
    if guess > secret:
        return TOO_HIGH


def main():
    # This while loop allows the game to be re-run

    while True:
        (low, high) = configure_range()
        secret = generate_secret(low, high)

        # Total guess counter is initialize with 0 at first
        count = 0

        while True:
            guess = get_guess()
            result = check_guess(guess, secret)
            # Add 1 count to guess counter when users guess
            count += 1
            print(result)

            if result == CORRECT:
                # If the guess is correct, show the counter
                print(f"Total guess: {count}")
                break

        print("Thanks for playing the game!")

        # This is where users get to choose if they want to play or not. Input is awaiting for users input to be any key or the "x" key. If users key choice is any key, rerun the game again, if it is x, then break and stop the game.
        user_choice = input("Press any key to start again. Press 'x' to exit game. ")

        # If user choice is "x", stop the game. The users input is converted to lowercase method is used to match the lower case "x" to be true. Specific if users want to use uppercase X.
        if user_choice.lower() == "x":
            break


if __name__ == "__main__":
    main()
