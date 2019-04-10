# This problem looks into buying and selling stocks once to maximize profit
# ex: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# Maximum profit that can be made with one buy and sell is 30 (260-290)


# Naive
# Time: O(n), Space: O(1)
def bns_stock_naive(A):
    min = A[0]
    difference = 0
    for i in range(1, len(A)):
        if A[i] > min: 
            if A[i] - min > difference:
                difference = A[i] - min
                min = A[i]
        else: min = A[i]
    return difference

# Solution
def bns_stock_sol(A):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


# Tests
test1 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
test2 = [5, 10, 15, 20, 25, 10, 30, 1, 0, 20]

def test(tests, func):
    for i in tests:
        print("tests: ", i, " --> ", func(i))

test([test1, test2], bns_stock_sol)
