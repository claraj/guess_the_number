import random


correct = "you guessed correctly!"
too_low = "too low"
too_high = "too high"


def configure_range():
    """Set the high and low values for the random number"""

    return 1, 1000 # Change range to be 1000 instead of 10.

  
def generate_secret(low, high):
    """Generate a secret number for the user to guess"""
    return random.randint(low, high)


def get_guess():
    """get user's guess, as an integer number"""
    # Users input validation
    # Used a while loop to keep asking for the correct input. If users input something other than an integer, then it throw an print exception in terminal and retry again, else return users' guessed number
    while True:
        try:
            users_input = int(input("Guess the secret number? "))

        except:
            # Print the error message to users.
            print("Input a integer please.")

        else:
            # Else, if everything passes, then return the users input number
            return users_input


def check_guess(guess, secret):
    """compare guess and secret, return string describing result of comparison"""
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    # This while loop allows the game to be re-run
    while True:
        (low, high) = configure_range()
        secret = generate_secret(low, high)

        while True:
            guess = get_guess()
            result = check_guess(guess, secret)
            print(result)


            if result == correct:
                break

    print("Thanks for playing the game!")

        # This is where users get to choose if they want to play or not. Input is awaiting for users input to be any key or the "x" key. If users key choice is any key, rerun the game again, if it is x, then break and stop the game.
        user_choice = input("Press any key to start again. Press 'x' to exit game. ")

        # If user choice is "x", stop the game. The users input is converted to lowercase method is used to match the lower case "x" to be true. Specific if users want to use uppercase X.
        if user_choice.lower() == "x":
            break


if __name__ == "__main__":
    main()
