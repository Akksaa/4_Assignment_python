MINIMUM_HEIGHT = 50

def main():
    height : int = int(input("How tall are you?\n"))

    while height <= MINIMUM_HEIGHT:
        print("You're not tall enough to ride, maybe next year!")
        height : int = int(input("How tall are you?\n"))
    
    print("You're tall enough to ride!")

if __name__ == "__main__":
    main()
