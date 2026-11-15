import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too Low! Try Again.")

            elif guess > secret_number:
                print("Too High! Try Again.")

            else:
                print("\nCongratulations! You Won!")
                print("Secret Number:", secret_number)
                print("Total Attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number!")


while True:
    guessing_game()

    play_again = input("\nPlay Again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break