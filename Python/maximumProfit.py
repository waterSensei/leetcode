prices = [1, 2, 3, 4, 5]


def maxProfit(prices) -> int:
    profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > buy:
            profit += prices[i] - buy
        buy = prices[i]
    return profit


print(maxProfit(prices))
