def solution(prices):
    answer = []
    until = len(prices)
    while prices:
        priceChangeUntilDrop = [prices[0]]
        for i in range(1, len(prices)):
            if priceChangeUntilDrop[0] <= prices[i]:
                priceChangeUntilDrop.append(prices[i])
            else:
                priceChangeUntilDrop.append(prices[i])
                break
        answer.append(len(priceChangeUntilDrop)-1)
        prices.pop(0)

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))