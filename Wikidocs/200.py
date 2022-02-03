ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
result = 0

for lst in ohlc[1:]:
        result += lst[0]-lst[3]

print(result)