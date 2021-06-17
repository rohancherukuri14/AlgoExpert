def nonConstructibleChange(coins):
    curr_change = 0
    coins.sort()
    for coin in coins:
        if coin > curr_change + 1:
            return curr_change + 1
        else:
            curr_change += coin
    return curr_change + 1