import random

roll_side = 6

def roll_dice():
    die1 = random.randint(1, roll_side)
    die2 = random.randint(1, roll_side)
    return die1, die2

def main():
    for i in range(3):
        die1, die2 = roll_dice()
        print(f"Roll {i + 1}: Die1 = {die1}, Die2 = {die2}")

if __name__ == "__main__":
    main()
