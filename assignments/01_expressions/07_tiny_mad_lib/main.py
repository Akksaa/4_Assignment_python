sentence_start : str = "GIAIC is fun. I learned programming and used Python to make my "


def main():

    adjective : str = input("Please enter an Adjective:\n")
    noun : str = input("Please enter a Noun:\n")
    verb : str = input("Please enter a Verb:\n")

    print(sentence_start + adjective + " "  + noun + " " + verb + "!")

if __name__ == "__main__":
    main()
