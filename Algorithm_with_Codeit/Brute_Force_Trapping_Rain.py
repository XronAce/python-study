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

    

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

"""
1. 처음 만나는 건물의 높이를 left_building으로 저장, lb_index도 저장
2. 처음 만나는 건물의 높이보다 더 큰 건물을 만나면 right_building으로 저장, rb_index도 저장. 만약 더 큰 건물이 없으면 그 중 가장 큰 건물을 right_building으로 저장, rb_index도 저장. 이 경우 인덱스가 가장 큰 것을 저장.
3. 저장된 index 값들을 이용하여 left_building, right_building 사이에 갖힌 trapped_rain을 세서 저장
4. trapped_rain을 한번이라도 계산한 경우, left_building에 right_building을 집어넣고 위 알고리즘 진행
"""