def isValidSubsequence(array, sequence):
    # Write your code here.
	prev_index = 0
	for val in sequence:
		if val not in array:
			return False
		else:
			new_index = array.index(val)
			if new_index < prev_index:
				return False
			prev_index = new_index
			array.remove(val)
	return True