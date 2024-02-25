import random

def roll_dice(num_dice):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls

def main():
    print("Welcome to the Dice Rolling App!")
    
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice <= 0:
                raise ValueError("Number of dice must be a positive integer.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")
    
    while True:
        rolls = roll_dice(num_dice)
        print(f"Rolling {num_dice} dice: {', '.join(map(str, rolls))}")

        choice = input("Would you like to roll again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thanks for using the Dice Rolling App!")
            break

if __name__ == "__main__":
    main()

