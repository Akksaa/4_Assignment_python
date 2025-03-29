import random

def main():
    dice_sides = 6

    die1 : int = random.randint(1, dice_sides)
    die2 : int = random.randint(1, dice_sides)
    total : int = die1 + die2

    print(f"Dices have {dice_sides} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


if __name__ == "__main__":
    main()
