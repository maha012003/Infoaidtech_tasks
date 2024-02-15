import random

def number_guessing_game():
    name = input("Welcome to the Number Guessing Game! What's your name? ")
    print(f"Hello, {name}! Let's play the game.")
    
    while True:
        random_number = random.randint(1, 100)
        attempts = 0
        
        print("I'm thinking of a number between 1 and 100.")
        print("You have 10 attempts to guess it.")
        
        while attempts < 10:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations, {name}! You've guessed the number {random_number} correctly in {attempts} attempts!")
                break
                
        if attempts == 10:
            print(f"Sorry, {name}. You've used all your attempts. The number was {random_number}.")
            
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing the game. Goodbye!")
            break

number_guessing_game()
