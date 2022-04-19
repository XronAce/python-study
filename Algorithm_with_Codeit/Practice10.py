def find_same_number(some_list):
    elements_seen_so_far = {}
    for number in some_list:
        if number not in elements_seen_so_far.keys():
            elements_seen_so_far[number] = True
        else:
            return number
    