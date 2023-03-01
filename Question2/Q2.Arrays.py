# //Merge Elements of two arrays A and B, Time Complexity: O(m+n)



# initializing NA as -1
NA = -1


# Function to move m elements at the end of array mPlusN[]
def moveToEnd(mPlusN, size):

	i = 0
	j = size - 1
	for i in range(size-1, -1, -1):
		if (mPlusN[i] != NA):

			mPlusN[j] = mPlusN[i]
			j -= 1


def merge(mPlusN, N, m, n): # Merges array N[] of size n into array mPlusN[] of size m+n
    
	i = n # Current index of i/p part of mPlusN[]
	j = 0 # Current index of N[]
	k = 0 # Current index of output mPlusN[]
	while (k < (m+n)):

		# Take an element from mPlusN[] if one of the following conditions are met:
		# a) Value of the picked element is smaller and we have not reached end of it
		# b) We have reached end of N[] */
		if ((j == n) or (i < (m+n) and mPlusN[i] <= N[j])):

			mPlusN[k] = mPlusN[i]
			k += 1
			i += 1

		else: # Otherwise take element from N[]

			mPlusN[k] = N[j]
			k += 1
			j += 1

# Function to print out an array on a line
def printArray(arr, size):

	for i in range(size):
		print(arr[i], " ", end="")

	print()

# Initialize arrays i.e. provide inputs
mPlusN = [1, 3, 5, 6, 8, NA, NA, NA]
N = [0, 2, 10]
n = len(N)

m = len(mPlusN) - n

# Move the m elements at the end of mPlusN
moveToEnd(mPlusN, m+n)

# Merge N[] into mPlusN[]
merge(mPlusN, N, m, n)

# Print the final result i.e. mPlusN
printArray(mPlusN, m+n)