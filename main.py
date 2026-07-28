import random
import sys
import time

# Main function for the game
def main():
    # While the player want to play the game
    while True:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 5 chances to guess the correct number.")
        print()
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")

        # Generate a random number to guess
        num = random.randint(1,100)

        # Initialize the chances
        chances = 0

        # Let user choose the difficulty levels
        while True:
            try:
                level = int(input("Enter your choice: "))
                if (level == 1):
                    chances = 10
                    print("Great! You have selected the Easy difficulty level.")
                    break
                elif (level == 2):
                    chances = 5
                    print("Great! You have selected the Medium difficulty level.")
                    break
                elif (level == 3):
                    chances = 3
                    print("Great! You have selected the Hard difficulty level.")
                    break
                else:
                    print("Difficulty level chosen was invalid. The available option is: 1 (Easy), 2 (Medium), or 3 (Hard). Try again!")
            except:
                print("Difficulty level chosen was invalid. The available option is: 1 (Easy), 2 (Medium), or 3 (Hard). Try again!")
                
        print("Let's start the game!")

        # Start the timer
        startTime = time.perf_counter()

        # Correct flag to see if user got the right ans or not
        correct = False

        # While the user still have the chances, let them guess
        i=0
        while i < chances:
            try:
                guess = int(input("Enter your guess: "))
                if guess == num:
                    print(f"Congratulations! You guessed the correct number in {(i + 1)} attempts.")
                    correct = True
                    break
                elif guess < num:
                    print(f"Incorrect! The number is greater than {guess}")
                    
                elif guess > num:
                    print(f"Incorrect! The number is less than {guess}.")
    
                i+=1
            except:
                print("Must enter an integer from 1-100")

        # If the user end up not getting the correct number, let them know the right number
        if not correct:
            print(f"Game Over! The correct number is: {num}")

        # Stop the timer 
        endTime = time.perf_counter()

        # Calculate the duration the player takes to guess
        duration = endTime - startTime

        print(f"Your guess took {duration:.4f} seconds")

        # Let the user choose if they want to play again
        while True:
            cont = input("Do you want to play again? (Y/N): ")
            if cont.lower() == 'y':
                break
            elif cont.lower() == 'n':
                sys.exit()
            else:
                print("Invalid choice! Type 'y' for yes or 'n' ")
if __name__ == "__main__":
    main()