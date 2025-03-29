import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('You guessed it wrong, Too low!')
        else:
            print("You guessed it wrong, Too high!")
    print(f"Yay, congrats! You guessed the number {random_number}")

def main():
    guess(23)

if __name__ == "__main__":
    main()
