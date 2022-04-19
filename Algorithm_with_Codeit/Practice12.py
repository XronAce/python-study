def trapping_rain(buildings):
    left_building = 0
    right_building = 0
    lb_index = 0
    rb_index = 0
    trapped_rain = 0
    flag = 0
    tallest_leftover = 0

    for i in range(0, len(buildings)):
        if buildings[i] != 0 and flag == 0:
            left_building = buildings[i]
            lb_index = i
            flag = 1
        elif buildings[i] > left_building:
            right_building = buildings[i]
            rb_index = i
            for j in range(lb_index+1, rb_index):
                trapped_rain += left_building - buildings[j]
            left_building = right_building
            lb_index = rb_index
        elif flag == 1:
            if buildings[i] >= tallest_leftover:
                right_building = buildings[i]
                tallest_leftover = buildings[i]
                rb_index = i
    
    for j in range(lb_index+1, rb_index):
        trapped_rain += right_building - buildings[j]

    return trapped_rain

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))