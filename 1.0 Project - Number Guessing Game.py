from random import randint

# Get the user's name and greet them
name = input("What is your name?: ")
print(f"Hello {name.capitalize()}! Let's play guess the number!")

# Get the minimum and maximum values for the guessing range
while True:
    try:
        min_val = int(input("Enter the minimum number: "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Please enter an integer value.\n")

while True:
    try:
        max_val = int(input("Enter the maximum number: "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Please enter an integer value.\n")

# Get the number of tries allowed
while True:
    try:
        num_tries = int(input("How many times would you like?: "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Please enter an integer value.\n")

# Generate a random number within the specified range
number = randint(min_val, max_val)

# Initialize the count of attempts
count = 1

# Main game loop
while count <= num_tries:
    # Get the user's guess
    guess = int(input("\nGuess the number: "))

    # Check if the guess is correct
    if guess == number:
        print(f"You guessed the number in {count} tries. Congratulations!")
        break  # Exit the loop if the guess is correct

    # Provide feedback if the guess is incorrect
    elif guess < number:
        print("Your guess is lower than the number.")
    else:
        print("Your guess is higher than the number")

    # Increment the count of attempts
    count += 1

# Check if the user ran out of tries
if count > num_tries:
    print(f"You couldn't guess the number in {num_tries} tries. The number was {number}.")
