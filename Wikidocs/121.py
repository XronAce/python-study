temp = input("Type any single letter regardless of capital or non-capital: ")

if temp.islower():
    print(temp.upper())
else:
    print(temp.lower())