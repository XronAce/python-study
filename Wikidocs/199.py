ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for lst in ohlc[1:]:
        if lst[3] > lst[0]:
                print(lst[1]-lst[2])