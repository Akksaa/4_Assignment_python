def get_lst():

    num_lst = []
    while True:
        input_num = input("Enter a number:\n")

        if input_num == "":
            break

        num : int = int(input_num)
        num_lst.append(num)

    return num_lst

def store_nums(num_lst):
    num_dict = {}

    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times!")

def main():
    num_lst = get_lst()
    num_dict = store_nums(num_lst)
    print_counts(num_dict)

if __name__ == "__main__":
    main()
