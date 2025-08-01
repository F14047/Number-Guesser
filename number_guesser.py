import random

rules = "Welcome to the Number Guessing game!\n" \
    "The rules are simple, select a difficulty\nand " \
    "try to guess the number between 1 and 100 " \
    "before your guesses run out."

input("Press Enter to start.\n")
print("\n" + "-"*50)
print (rules)

# Select difficulty
def select_diff():
    global lives
    while True:
        print("Select a difficulty level: Easy / Medium / Hard")
        diff = input().lower()
        if diff == 'easy':
            lives = 5
            break
        elif diff == 'medium':
            lives = 3
            break
        elif diff == 'hard':
            lives = 1
            break
        else:
            print("Invalid difficulty level." \
            " Please choose Easy, Medium, or Hard.")

    print(f"You have {lives} {"chance" if lives == 1 else "chances"} to guess.\n")



# Score
score = 0

def play_game():
    global lives, score

    # Randomly selects an integer from 1 to 100.
    answer = random.randint(1, 100)

    # Attempt counter.
    counter = 0
    
    while lives > 0:
        try:
            guess = int(input("Guess a number from 1 to 100: \n"))
        except ValueError: 
            print("Please enter a valid integer between 1 and 100.\n")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a positive integer between 1 and 100.")
            continue
        
        counter += 1
        if guess == answer:
            score += 1
            print(f"\n Congratulations! You guessed the number in {counter} {'attempt' if counter == 1 else 'attempts'}!")
            break
        else:
            lives -= 1
            if guess < answer:
                print("Too low.")
            else:
                print("Too high.")
            if lives > 0:
                print(f"You have {lives} {'guess' if lives == 1 else 'guesses'} left.\n")
            else:
                print(f"\nYou're out of guesses. The correct number was {answer}.")


# Start the game
while True:
    select_diff()
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again == 'y':
        select_diff()
        play_game()
    if again != 'y':
        print("Thanks for playing!\n")
        print(f"Your score is {score}.")
        break
