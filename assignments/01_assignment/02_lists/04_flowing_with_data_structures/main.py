def three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    my_list = []
    message = input("Enter a message to copy:")
    print("List Before:", my_list)
    three_copies(my_list, message)
    print("List After:", my_list)


if __name__ == "__main__":
    main()
