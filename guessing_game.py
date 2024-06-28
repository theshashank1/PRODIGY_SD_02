import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)

def get_feedback(guess, target):
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def play_game():
    target_number = generate_random_number()
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            feedback = get_feedback(guess, target_number)
            print(feedback)
            if feedback == "Correct!":
                guessed_correctly = True
                print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_game()
