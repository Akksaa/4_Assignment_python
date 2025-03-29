import math

def main():
    perp : float = float(input("Enter the length of AB (the perpendicular) :\n"))
    base : float = float(input("Enter the length of AC (the base) :\n"))

    hyp : float = math.sqrt(perp**2 + base**2)
    print("The length of BC (the hypotenuse) is:", str(hyp))


if __name__ == "__main__":
    main()
