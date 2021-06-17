def sortedSquaredArray(array):
    new_arr = [abs(i) for i in array]
    new_arr.sort
    return [i**2 for i in new_arr]