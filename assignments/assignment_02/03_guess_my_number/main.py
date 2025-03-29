import random

def main():
    print("Guess my number")
    SECRET_NUM = random.randint(1,120)

    print("I'm thinking of a number between 1 and 120...")

    guess = int(input("Enter your guess:"))

    while guess != SECRET_NUM:
        if guess > SECRET_NUM:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")

        print()
        guess = int(input("Enter a new guess:"))
    
    print("Congrats! You guessed the number, it was " + str(SECRET_NUM))

if __name__ == "__main__":
    main()

