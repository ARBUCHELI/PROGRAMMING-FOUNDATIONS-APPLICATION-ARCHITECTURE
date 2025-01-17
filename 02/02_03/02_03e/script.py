import random

def main():
    print("Welcome to the Guess the Number game!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    print("I have selected a number between 1 and 100.")
    
    while True:
        try:
            # Prompt the user to enter a guess
            guess = int(input("Can you guess the number? "))
            
            # Check if the guess is correct, too high, or too low
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number.")
                break  # Exit the loop if the guess is correct
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
