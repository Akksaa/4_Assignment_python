def main():
    user_input : str = input("Type a number to see its square: \n")
    squared_num : int = int(user_input) ** 2
    print(f"The square of {user_input} is {squared_num}!")
    

if __name__ == "__main__":
    main()
