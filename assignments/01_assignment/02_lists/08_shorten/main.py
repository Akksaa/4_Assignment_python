MAX_LENGTH = 4

def shorten(lst):

    print("List before shortening:", lst)
    if len(lst) > MAX_LENGTH:
        for i in range(0,len(lst)):
            removed_elem = lst.pop()
            print(removed_elem, "removed!")
        
        print("List after shortening:", lst)
    else:
        print("Add more items to the list!")

def get_lst():

    lst = []
    elem = input("Enter a value to add to the list or press Enter to exit\n")

    while elem != '':
        lst.append(elem)
        elem = input("Enter a value to add to the list or press Enter to exit\n")
    return lst
        

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == "__main__":
    main()
