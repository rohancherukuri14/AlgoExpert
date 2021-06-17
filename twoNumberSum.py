def twoNumberSum(array, targetSum):
    lookup = []
    for num in array:
        diff = targetSum - num
        if diff in lookup:
            return [diff, num]
        else:
            lookup.append(num)
    return []