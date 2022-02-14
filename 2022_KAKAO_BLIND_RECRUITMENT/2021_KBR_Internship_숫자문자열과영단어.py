def solution(s):
    answer = ""
    temp = ""
    letter = {"zero":0, "one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    
    for i in s:
        if i.isalpha():
            temp += i
            if temp in letter.keys():
                answer += str(letter[temp])
                temp = ""
        else:
            answer += i
            
    return int(answer)

# s = "one4seveneight"
# print(solution(s))