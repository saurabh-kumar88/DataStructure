
"kadane's algorithm"

"reference : https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d "

def kadane_max(arr):
  
	local_max, global_max = 0, float('-inf')
  
	for number in arr:
		local_max =  max( number, (local_max + number) )
		if local_max > global_max:
			global_max = local_max

	return global_max
			

arr = [ -1, 2, 3, -6, -5 ] 


if __name__ == "__main__":
    print( kadane_max(arr)	)

		