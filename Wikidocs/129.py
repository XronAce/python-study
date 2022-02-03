resNo = input("Please enter your residence number\(ex. 123456-7890123\): ")
lst = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
cal = 0

resNo = resNo.replace("-", "")

for i in range(0, len(lst)):
    cal = cal + int(resNo[i])*lst[i]

modulo = cal % 11
isValid = 11 - modulo

if isValid == int(resNo[-1:]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")