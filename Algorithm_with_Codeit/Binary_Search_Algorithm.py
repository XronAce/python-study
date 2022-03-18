def binary_search(element, some_list):
    stidx = 0
    edidx = len(some_list)-1
    mdidx = (edidx+stidx)//2
    flag = 0
    count = 0
    
    while flag == 0:
        if some_list[mdidx] == element:
            return mdidx
        elif some_list[mdidx+1] == element:
            return mdidx+1
        elif some_list[mdidx] > element:
            edidx = mdidx
            mdidx = (edidx+stidx)//2
            count += 1
        else:
            stidx = mdidx
            mdidx = (edidx+stidx)//2
            count += 1
  

        if count > 50:
            break
        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))