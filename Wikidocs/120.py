fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
temp = input("좋아하는 과일은? ")

if temp in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")