def binary_search(element, some_list):
    stidx = 0
    edidx = len(some_list)-1
    mdidx = (edidx+stidx)//2
    
    while True:
        if some_list[mdidx] == element:
            return mdidx
        elif some_list[mdidx+1] == element:
            return mdidx+1
        elif some_list[mdidx] > element:
            edidx = mdidx
            mdidx = (edidx+stidx)//2
            if mdidx == 0:
                if some_list[mdidx] == element:
                    return mdidx
                else:
                    return None
        else:
            stidx = mdidx
            mdidx = (edidx+stidx)//2
            if mdidx == len(some_list)-2:
                if some_list[mdidx] == element:
                    return mdidx
                elif some_list[mdidx+1] == element:
                    return mdidx+1
                else:
                    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))