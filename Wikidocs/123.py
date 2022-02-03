temp = input("Please enter your currency: ")
currency = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
money = temp.split(" ")

print(f"{float(money[0])*currency[money[1]]} 원")