resNo = input("Please enter your residence number\(ex. 123456-7890123\): ")

if int(resNo[7]) in [1, 3]:
    print("Male")
else:
    print("Female")