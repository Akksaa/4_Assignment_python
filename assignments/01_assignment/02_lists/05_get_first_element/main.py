def get_first_elem(my_list):
    print("First element of the list:",my_list[0])

def get_list():
    my_list = []
    element: str = input("Enter an element to add in the list or press Enter to stop.\n")

    while element != "":
        my_list.append(element)
        element: str = input("Enter an element to add in the list or press Enter to stop.\n")
    return my_list

def main():
    my_list = get_list()
    get_first_elem(my_list)


if __name__ == "__main__":
    main()

