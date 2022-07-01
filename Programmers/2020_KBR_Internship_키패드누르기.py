def solution(numbers, hand):
    left_loc = 10
    right_loc = 11
    position = [(3,1), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (3,0), (3,2)] # keypad location in array, 0, 1, 2, ... , *, #
    answer = ""

    for number in numbers:
        if number in [1, 4, 7]:
            left_loc = number
            answer += 'L'
        elif number in [3, 6, 9]:
            right_loc = number
            answer += 'R'
        else:
            distLeft = abs(position[number][0]-position[left_loc][0]) + abs(position[number][1]-position[left_loc][1])
            distRight = abs(position[number][0]-position[right_loc][0]) + abs(position[number][1]-position[right_loc][1])
            if distLeft > distRight:
                right_loc = number
                answer += 'R'
            elif distLeft < distRight:
                left_loc = number
                answer += 'L'
            else:
                if hand == "left":
                    left_loc = number
                    answer += 'L'
                else:
                    right_loc = number
                    answer += 'R'
            
    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'
# print(solution(numbers, hand))