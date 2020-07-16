import math

"Implementation of Jump search algo, search index of element 55"
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
Jump_next = 4
N = len(arr)
target = 55


# STEP 1: Jump from index 0 to index 4;
# STEP 2: Jump from index 4 to index 8;
# STEP 3: Jump from index 8 to index 12;
# STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8.
# STEP 5: Perform linear search from index 8 to get the element 55.


def JumpSearch( arr , x , n ): 
      
    # Finding block size to be jumped 
    step = math.sqrt(n) 
      
    # Finding the block where element is 
    # present (if it is present) 
    prev = 0
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        step += math.sqrt(n) 
        if prev >= n: 
            return -1
      
    # Doing a linear search for x in  
    # block beginning with prev. 
    while arr[int(prev)] < x: 
        prev += 1
          
        if prev == min(step, n): 
            return -1

    if arr[int(prev)] == x: 
        return prev 
      
    return -1
        

if __name__ == "__main__":
    
    print( JumpSearch(arr, 145, len(arr)) )
 
        

        


