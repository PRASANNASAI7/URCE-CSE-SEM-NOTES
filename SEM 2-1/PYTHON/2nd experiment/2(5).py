def perform_operations():
    my_list = [10, 20, 30, 40, 50]
    print("original list:",my_list)
    my_list.append(60)
    print("after addition:",my_list)

    my_list.insert(2, 25)  # Insert 25 at index 2
    print("after insertion:",my_list)

    sliced_list = my_list[1:4]  # Extract elements from index 1 to 3 (4 is excluded)
    print("after sliced operation:",sliced_list)
perform_operations()
