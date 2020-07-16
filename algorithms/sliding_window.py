# -------------------------- sliding window algorithm ----------------------

# O(n) solution for finding 
# maximum sum of a subarray of size k 
import sys 
INT_MIN = -sys.maxsize -1

def maxSum(arr, n, k): 

	# n must be greater than k 
	if not n > k: 
		print("Invalid") 
		return -1

	# Compute sum of first window of size k 
	max_sum = INT_MIN 
	window_sum = sum(arr[:k]) 

	# Compute sums of remaining windows by 
	# removing first element of previous 
	# window and adding last element of 
	# current window. 
	for i in range(n-k): 
		window_sum = window_sum - arr[i] + arr[i + k] 
		max_sum = max(window_sum, max_sum) 

	return max_sum

# driver code

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
k = 4
n = len(arr)
if __name__ == "__main__":
    
  print(maxSum(arr, n, k))
  