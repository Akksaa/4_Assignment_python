def main():
    name: str = input("Enter a Name:")
    noun : str = input("Enter a Noun:")
    animal : str = input("Enter an Animal:")
    verb : str = input("Enter a Verb:")
    adjective : str = input("Enter an Adjective:")
    place : str = input("Enter a Place:")
    food : str = input("Enter a Food:")
    feeling : str = input("Enter a Feeling:")
    
    story = f"""
    Once upon a time, in the magical land of {place}, there was a {adjective} {noun} named {name}.
    {name} loved to explore the forests and talk to the friendly {animal}s that lived there.

    One day, while {name} was wandering around, they discovered a hidden path leading to a secret garden.
    In the middle of the garden, there was a golden table filled with delicious {food}.
    {name} was so {feeling} that they couldn't resist but {verb} with joy!

    Suddenly, a wise old {animal} appeared and said, "To unlock the true magic of this place, you must always follow your heart."
    {name} smiled, knowing that this adventure was just the beginning of many more to come!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
