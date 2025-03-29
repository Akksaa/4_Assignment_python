
def add_numbers(numbers) -> int :
    total : int = 0
    for num in numbers:
        total = total + num
    
    return total

def main():
    my_numbers : list = [1,2,3,4,5]
    sum_of_numbers : int = add_numbers(my_numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()
