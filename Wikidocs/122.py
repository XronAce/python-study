score = int(input("Please enter your score: "))

if score <= 20:
    print("grade is E")
elif 20 < score <= 40:
    print("grade is D")
elif 40 < score <= 60:
    print("grade is C")
elif 60 < score <= 80:
    print("grade is B")
else:
    print("grade is A")