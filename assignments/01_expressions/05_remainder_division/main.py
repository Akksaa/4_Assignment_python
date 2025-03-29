def main():
    dividend : int = int(input("Enter an integer to be divided:\n"))
    divisor : int = int(input("Enter an integer to divide by:\n"))

    quotient : int = dividend // divisor
    remainder : int = dividend % divisor

    print(f"The result of this division is {quotient} with a remainder of {remainder}!")

if __name__ == "__main__":
    main()
