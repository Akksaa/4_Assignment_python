PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    user_age : int = int(input("How old are you?"))

    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You can not vote in Peturksbouipo where the voting age is 16.")

    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlu where the voting age is 25.")
    else:
        print("You can not vote in Stanlu where the voting age is 25.")

    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayngua where the voting age is 48.")
    else:
        print("You can not vote in Mayngua where the voting age is 48.")


if __name__ == "__main__":
    main()
