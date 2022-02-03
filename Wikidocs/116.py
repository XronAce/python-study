temp = input("Please enter current time: ")

if temp[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")