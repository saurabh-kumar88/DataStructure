import math
# arr[] ==> Input sorted array where search need to be preformed
# search_item     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]


class Search_algorithms(object):
    def __str__(self):
        return "Description : Container class for different search algorithms"

    def __init__(self, arr, search_item):
        self.arr = arr
        self.search_item = search_item
        self.length = len(arr)
    
    def binary_search(self):
        "complexity : O(logn)"

        if len(self.arr) == 0:
            return None
        lo = 0
        hi = len(self.arr)

        while lo <= hi:
            mid = int( lo + (hi - lo)/2 )

            if self.search_item == self.arr[mid]:
                return mid
            
            if self.search_item < self.arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return None
    
    
    def interpolation_search(self):
        "complexity : O(log(logn)) or worse case O(n)"

        lo = 0
        hi = len(self.arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) * (self.search_item - self.arr[lo]) // (self.arr[hi] - self.arr[lo])

            if mid > hi or mid < lo:
                return None
            
            if self.search_item == self.arr[mid]:
                return mid

            if self.search_item < self.arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return None

    def jump_search(self):
        "complexity : O(sqrt(n))"
        
        if self.length == 0:
            return None
        lo = 0
        hi = self.length - 1
    
        step = int( math.sqrt( self.length ) )
        prev = 0

        while step <= hi:    
            if self.search_item == self.arr[step]:
                return step

            if self.search_item > self.arr[step]:
                prev = step
                step += int( math.sqrt( self.length ) )
            
            if self.search_item < self.arr[step]:
                while self.search_item < self.arr[prev]:
                    if self.search_item == self.arr[prev]:
                        return prev
                    prev += 1
        return None


                     
            
    
if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    arr2 = []
    obj = Search_algorithms( arr,  19 )
    # print( obj.interpolation_search() )
    # print( obj.binary_search() )
    print( obj.jump_search() )
    
        






