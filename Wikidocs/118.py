warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

temp = input("Enter any investment name: ")

if temp in warn_investment_list:
    print("It is a warning investment list.")
else:
    print("It is not a warning investment list.")