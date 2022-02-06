f = open("C:/Users/XronoCore/Desktop/매수종목1.txt", "r", encoding="utf8")

lst = []
lst.append(f.readline().strip())
lst.append(f.readline().strip())
lst.append(f.readline())

f.close()

print(lst)