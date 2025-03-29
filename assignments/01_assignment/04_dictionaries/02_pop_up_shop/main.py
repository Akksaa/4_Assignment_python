FRUITS = {
    "Apple": 1.5,
    "Raspberry": 7.5,
    "Kiwi": 9,
    "Mango": 7,
    "Strawberry": 10,
    "Melon": 5.80

}

def main():
        total_cost = 0
        for fruit in FRUITS:
            price = FRUITS[fruit]
            amount = int(input(f"How many {fruit} do you want?: "))
            total_cost += price * amount
        
        print("Your total is $" + str(total_cost))


if __name__ == "__main__":
    main()
