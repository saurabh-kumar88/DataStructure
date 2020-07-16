def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)

    arr.clear()
    while ( len(L) > 0 and len(R) < 0 ):
      if L[0] <= R[0]:
        arr.append(L[0])
        L.pop(0)
      else:
        arr.append(R[0])
        R.pop(0)
      
      for i in L:
        arr.append(i)
      
      for j in R:
        arr.append(j)

# driver code
arr = [12,11,45,9,-1,56]

def printList(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()


if __name__ == "__main__":
    
    print("original :", *arr)
    mergeSort(arr)
    print("After sorting : ")
    printList(arr)
