from random import randint

name = input("What is your name?: ")
print(f"Hello {name.capitalize()}! Let's play guess the number!")

while True:
    try:
        min_val = int(input("Enter the minimum number: "))
        break
    except ValueError:
        print("Please enter an integer value.\n")

while True:
    try:
        max_val = int(input("Enter the maximum number: "))
        break
    except ValueError:
        print("Please enter an integer value.\n")

while True:
    try:
        num_tries = int(input("How many times would you like?: "))
        break
    except ValueError:
        print("Please enter an integer value.\n")

number = randint(min_val, max_val)

count = 1

while count <= num_tries:
    guess = int(input("\nGuess the number: "))

    if guess == number:
        print(f"You guessed the number in {count} tries. Congratulations!")
        break

    elif guess < number:
        print("Your guess is lower than the number.")

    else:
        print("Your guess is higher than the number")

    count +=1

if count > num_tries:
    print(f"You couldn't guess the number in {num_tries} tries. The number was {number}.")