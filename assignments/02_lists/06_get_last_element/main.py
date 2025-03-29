def get_last_item(lst):
    print("Last item of the list:", lst[-1])

def get_lst():
    lst = []
    element: str = input("Enter an element to add in the list or press Enter to stop.\n")

    while element != "":
        lst.append(element)
        element: str = input("Enter an element to add in the list or press Enter to stop.\n")
    return lst

def main():
    lst = get_lst()
    get_last_item(lst)


if __name__ == "__main__":
    main()

