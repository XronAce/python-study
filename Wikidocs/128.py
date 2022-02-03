resNo = input("Please enter your residence number\(ex. 123456-7890123\): ")

if int(resNo[9]) in range(0,9):
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")