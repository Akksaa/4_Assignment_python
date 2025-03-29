import random

def guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = x
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay, the computer guessed your number, {guess}, correctly! ")


def main():
    guess(20)

if __name__ == "__main__":
    main()
