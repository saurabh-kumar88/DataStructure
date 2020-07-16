import cmath
import sys
import math
from functools import reduce
import numpy as np

def print_elements(A, index):
  
  if index > len(A)-1:
    return
  else:
    print( A[index], end=" " )
    index += 1
    print_elements( A, index )
    

def fib(n):
  if n == 0:
    return 0
  
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)


def fac(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * fac( n - 1 )
    
  

arr = ['foo', 'bar', 'is', 'cool']


def power_of_four(num):
  # Boundary conditions
  INT_MIN = -sys.maxsize 
  INT_MAX = sys.maxsize - 1
  if num < INT_MIN or num > INT_MAX:
    return False
  
  if math.log(num, 4) == int(math.log(num, 4)):
    return True
  else:
    return False


def reverse_string(string, i):
  
  if i > len(string) :
    return
  else:
    print(string[-i], end=" ") 
    i += 1
    reverse_string(string, i)


# print all possible word formation from mobile keypad for a given 3 digit number [2-9]



# without recursion

def keypad_wordFormation(arr):

  # corner condition 
  # return if key error
  
  mobile_keypad = { 
  2 : "ABC",
  3 : "DEF",
  4 : "GHI",
  5 : "JKL",
  6 : "MNO",
  7 : "PRQS",
  8 : "TUV",
  9 : "WXYZ",}

  str1 = mobile_keypad[ arr[0] ]
  str2 = mobile_keypad[ arr[1] ]
  str3 = mobile_keypad[ arr[2] ]

  s3 = 0
  while s3 < len(str3):
    for j in range(len(str2)):
      for i in range(len(str1)):
        print( str1[i]+str2[j]+str3[s3] )
      print()
    
    s3 += 1

"Replace each element of array by product of rest of elements in O(n) time"
def product_replace(arr, i):
  
  left_sub = [] #  product of [0..i-1]
  right_sub = [] # product [i+1....n-1]

  n = len(arr)
  
  if i > n-1:
    return
  
  if i == 0:
    right_sub = np.prod(arr[ 1 : n ]) 
    left_sub = 1

  if i == n:
    left_sub = np.prod(arr[ 0 : i-1])
    right_sub = 1

  left_sub = np.prod(arr[ 0 : i-1 ])
  right_sub = np.prod(arr[ i+1 : n ]) 

  arr[i] = int( left_sub * right_sub )
    
  i += 1

  product_replace(arr, i)

  return arr





if __name__ == "__main__":
  # print_elements(arr, 0)
  
  # n = 7
  # for i in range(0, n):
  #   print(fib(i), end=" ")

  # print(fac(0))

  # print( power_of_four(-sys.maxsize ) )
  
  # reverse_string("foo bar", 1)

  # keypad_wordFormation([2,3,4]) 
  a = [1,2,3,4,6]
  print( product_replace(a , 0 ) )
  # print( reduce( (lambda x,y: x * y), [1,2,3] ) )
  
  # arr = [ 1,2,3 ]
  # print( np.prod(arr) )  

  
    