"merge sort"

# driver code
Arr = [45,13,29,87,44,39]

def mergeSort(arr):

  # base case
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i] ,end=" ") 
	print()


      
if __name__ == "__main__":
  print("original array : ", Arr)
  mergeSort(Arr)
  print("after sorting : ", end="\n")
  printList(Arr)
  


















  





      











