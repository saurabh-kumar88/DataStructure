from collections import Counter
def boyer_moore_voting(arr):
    candidate = None
    count = 0
    # arr.sort()
    # print(arr)
    for value in arr:
        if count == 0:
            candidate = value
        count += (1 if candidate == value else -1)
 
    # Condition for majority test        
    # if count > len(arr)//2:
    #     return candidate
    return candidate
   
    

arr = [ -1,12,12,45,63,63,63,63,63,63,6,6,6,6,6,6,6,6,6 ]
# arr2 = [1,2,3,4,5,6,7,8,9]
if __name__ == "__main__":
    print("Majority : ", boyer_moore_voting(arr) )
    # print( len(arr), len(arr)//2 )
    # print( Counter(arr) )

    # Sorting Approach
    # arr.sort()
    # mid = len(arr)//2
    # print("[n/2]", mid)
    # print("Majority at arr[mid] : ", arr[mid])
    
    