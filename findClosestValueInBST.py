def findClosestValueInBst(tree, target):
    # Write your code here.
	return helper(tree, target, tree.value)
    
def helper(tree, target, nearest):
	if tree is None:
		return nearest
	if abs(target - tree.value) < abs (target-nearest):
		nearest = tree.value
	if target < tree.value:
		return helper(tree.left, target, nearest)
	elif target > tree.value:
		return helper(tree.right, target, nearest)
	else:
		return nearest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None