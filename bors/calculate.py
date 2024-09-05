def calculate_max_difference(prices):
    max_diff = 0
    min_value = prices[0]
    max_pair = (prices[0], prices[0])

    for price in prices:
        if price < min_value:
            min_value = price
        current_diff = price - min_value
        if current_diff > max_diff:
            max_diff = current_diff
            max_pair = (min_value, price)

    return max_diff, min_value, max_pair
