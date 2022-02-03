data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result1 = []

for lst in data:
    result = []
    for i in lst:
        result.append(i * 1.00014)
    result1.append(result)
print(result1)