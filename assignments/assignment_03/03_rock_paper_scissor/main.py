import random

def main():
    user = input("What's you choice? 'r' for rock, 's' for scissor and 'p' for paper:")
    computer = random.choice(['s', 'p', 'r'])
    print(f"User's choice: {user}")
    print(f"Computer's choice: {computer}")

    if user == computer:
        print("It's a tie!")

    if is_win(user, computer):
        print("Yay, you won!")
    else:
        print("You lost!")

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True


if __name__ == "__main__":
    main()
