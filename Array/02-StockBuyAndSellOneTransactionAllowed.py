# Naive Approach: By exploring all possible pairs - T.C: O(n**2) & S.C: O(1)
def max_profit(prices):
    n = len(prices)
    res = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    
    return res

# Expected Approach: T.C: O(n) & S.C: O(1)
def maxProfit2(prices):
    least = prices[0]
    profit = 0
    
    # Get the least value till i
    for i in range(len(prices)):
        least = min(least, prices[i])
        profit = max(profit, prices[i] - least)
    
    return profit

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(max_profit(prices))