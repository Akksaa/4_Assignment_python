
inches_in_foot = 12

def main():
    input_feet : float = float(input("Enter number of feets:"))
    feet_to_inches : float = input_feet * inches_in_foot
    print(str(input_feet),"feet = " , str(feet_to_inches), "inches!")

if __name__ == "__main__":
    main()
