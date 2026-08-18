# arr = [10, 20, 30, 40, 50]
# sufix = [4]*len[5]
# sufix[4]= nums[4]

# for i in range (2, -1, -1):
#     suffix[i]= = suffix[i+1] + nums[i]
# return suffix 



# LEETCODE: 121. Best Time to Buy and Sell Stock
def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit