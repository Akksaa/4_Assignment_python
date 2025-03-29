def main():
    side_1 : float = float(input("What is the length of side 1?\n"))
    side_2 : float = float(input("What is the length of side 2?\n"))
    side_3 : float = float(input("What is the length of side 3?\n"))

    result : float = side_1 + side_2 + side_3
    print(f"The perimeter of the triangle is {result}")
    

if __name__ == "__main__":
    main()
