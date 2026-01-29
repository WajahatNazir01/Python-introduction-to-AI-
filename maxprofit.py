#You are given an array of prices where prices[i] is the price of a given stock on the i-th day. You want to maximize your profit by choosing one single day to buy one stock and choosing a different day in the future to sell that stock.
def max_profit(prices):
    min_price = float('inf')
    max_p = 0
    
    for price in prices: # 'price' is the actual value (e.g., 7, 1, 5...)
        # 1. Update min_price if current price is a new low
        if price < min_price:
            min_price = price
        
        # 2. Calculate potential profit if we sold today
        current_profit = price - min_price
        
        # 3. Update max_p if this is the best profit so far
        if current_profit > max_p:
            max_p = current_profit
            
    # Return ONLY after the loop has finished checking every day
    return max_p

# Test it
print(max_profit([7, 1, 5, 3, 6, 4])) # Should output 5