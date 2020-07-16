def knapSack(val, weight, cap, n):
  # base case
  if n == 0 and cap == 0:
    return 0
  elif weight[n - 1] > cap:
    return knapSack(val, weight, cap, n-1) # shift pointer to left
  else:
    return max( val[n-1], knapSack(val, weight, cap-weight[n-1], n-1), knapSack(val, weight, cap, n-1) ) 



# driver code
values = [5,3,5,3,2] # values if $
weight = [1,2,4,2,5] # weight in Kg
capacity = 10 # knapsack capacity
n = len(values) - 1


def KS(n, C):
  if n==0 and C==0:
    return 0
  elif weight[n] > C:
    return KS(n-1, C)
  else:
    temp1 = KS(n-1, C)
    temp2 = values[n-1] + KS(n-1, C-weight[n])
    result = max(temp1, temp2)
  return result


if __name__ == "__main__":
    # print( knapSack(values, weight, capacity, n) )
    # print(KS(n, capacity))
    print(weight[n])



