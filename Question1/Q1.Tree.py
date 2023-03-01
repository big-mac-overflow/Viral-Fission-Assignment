# //InOrder Tree Traversal, Time Complexity: O(n)



# A class that represents an individual node in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


#function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		printInorder(root.right)


# Inputting tree here
if __name__ == "__main__":
	root = Node(7)
	root.left = Node(2)
	root.right = Node(4)
	root.left.left = Node(3)
	root.left.right = Node(1)

	# Invoking Function
	print ("\nInorder traversal of binary tree is")
	printInorder(root)