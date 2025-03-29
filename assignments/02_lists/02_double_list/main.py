def main():

    my_list : list[int] = [1,2,3,4,5]
    print("Original list: ", my_list)

    for i in range(len(my_list)):
        element_at_index = my_list[i]
        my_list[i] = element_at_index * 2

    print("Doubled list: ",my_list) 

if __name__ == "__main__":
    main()
