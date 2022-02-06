f = open("C:/Users/XronoCore/Desktop/매수종목2.txt", "r", encoding="utf8")

lst = []
data = {}
lines = f.readlines()

print(lines)
for line in lines:
    line = line.strip()
    k, v = line.split()
    data[k] = v

f.close()

print(data)