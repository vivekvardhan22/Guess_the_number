import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Set the number of guesses to 3
guesses = 3

# Print the instructions
print("Welcome to the guessing game!")
print("I have chosen a number between 1 and 10.")
print("You have 3 guesses to find it.")

# Loop until the user runs out of guesses or finds the number
while guesses > 0:
    # Prompt the user for a guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == number:
        # Congratulate the user and end the game
        print("You got it! The number was", number)
        break
    else:
        # Give feedback and reduce the number of guesses
        if guess < number:
            print("Too low.")
        else:
            print("Too high.")
        guesses -= 1

# Check if the user ran out of guesses
if guesses == 0:
    # Reveal the number and end the game
    print("Sorry, you ran out of guesses. The number was", number)