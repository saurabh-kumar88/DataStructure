def count_sort(A):
  
  freq = Counter(A)
  
  n = len(A)
  values = [x for x in range(n)] # count values of all numbers (weather exist in freq.keys() or not)
  ans = [None for x in range(n)] # we will write our sorted array here

  # get count values of all numbers (range 0 to len(A))
  for i in range(0, n):
    if i in sorted(freq.keys()):
      values[i] = freq[i] 
    else:
      values[i] = 0

  # modify values (add previous value to current value )
  for x in range(0, len(values)):
    values[x] += values[x-1]

  for i in range(n):
    j = values[i]
    while j > 0:
      if ans[j-1] is None:
        ans[j-1] = i
      j -= 1
  return ans
  
  

arr = [7,1,3,1,2,4,5,7,2,4,3]

if __name__ == "__main__":
    
    print(count_sort(arr))