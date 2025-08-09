import random

if __name__ == "__main__":
    min, max = map(int, input("Input min, max values (comma separated): ").split(","))

    secret_number = random.randint(min, max)

    while True:
        guess_number = int(input(f"Guess a number between {min} and {max}: "))

        if guess_number == secret_number:
            print("Congratulations! You've guessed the right number.")
            break
        elif guess_number < secret_number:
            print("Try again! The secret number is higher.")
        else:
            print("Try again! The secret number is lower.")