def pickup_even(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    
    print(even_list)

pickup_even([3, 4, 5, 6, 7, 8])