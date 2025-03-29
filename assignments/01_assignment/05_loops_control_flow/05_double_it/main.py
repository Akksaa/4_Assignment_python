def main():
    
    curr_value = int(input("Enter a number:\n"))

    while curr_value < 100:
        curr_value *= 2
        print(f'Doubled value: {curr_value}')


if __name__ == "__main__":
    main()
