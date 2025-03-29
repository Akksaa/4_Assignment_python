def add_phone_numbers():

    phonebook = {}
    while True:
        name = input("Enter a name:\n")

        if name == "":
            break

        contact = input("Enter the contact number:\n")

        if contact == "":
            break

        phonebook[name] = contact
    return phonebook

def show_phonebook(phonebook):
    for name in phonebook:
        print(name + " -> " + phonebook[name])

def lookup_contact(phonebook):
    while True:
        name = input("Enter a name to lookup:\n")

        if name == "":
            break

        if name not in phonebook:
            print(name + " is not saved in the phonebook!")
        else:
            print(name + " -> " + phonebook[name])



def main():
    phonebook = add_phone_numbers()
    show_phonebook(phonebook)
    lookup_contact(phonebook)


if __name__ == "__main__":
    main()
