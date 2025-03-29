def get_lst():
    lst = []
    elem: str = input("Enter a value:\n")
    while elem != "":
        lst.append(elem)
        elem: str = input("Enter a value:\n")
    return lst

def main():
    lst = get_lst()
    print("Here is the list:", lst)
    
if __name__ == "__main__":
    main()
