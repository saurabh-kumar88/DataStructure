#_____________________ Implementation of Hash-Map using Linear probing __________________

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range (self.MAX)]
    
    def __str__(self):
        return "Hash-map Implementation in python"
        
    def get_key(self,key):
        self.key = key
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # using python's magic methods 
    def __setitem__(self, key, val):
        h = self.get_key(key)
        
        # check if key is already present in list and also check if free space availabe for new entry 
        if self.arr[h]:
            print("colision occurred")
            __memory_capacity_full = True
            for search_index in range(self.MAX):
                if self.arr[search_index] is None:
                    self.arr[search_index] = val
                    __memory_full = False
                else:
                    __memory_full = True
            if __memory_full:
                print("No free space availabe, memory max capacity reached!")
        else:
            self.arr[h] = val
        
    def __getitem__(self, key):
        self.key = key
        h = self.get_key(key)
        found = False
        # Check if key exists
        if self.arr[h]:
            return 'Value : {} '.format(self.arr[h])
            found = True
        if not found:
            raise Exception('{} is not a valid key'.format(self.key))
                
            
    def __delitem__(self, key):
        h = self.get_key(key)
        found = False
        # Check if key exists
        if self.arr[h]:
            del self.arr[h]
            found = True
            return 'item deleted!'
        if not found:
            raise Exception('{} is not a valid key'.format(key))


if __name__ == "__main__":
    obj = HashTable()
    
    # Test to check exception for memory capacity reached 
    # for i in range(obj.MAX):
    #     obj.arr[i] = i
    # print(obj.arr)
    
    # write, read/update & delete operations
    # obj['Jan 1'] = 'Jan 1 is 32'
    # print(obj['Jan 1'])
    # del obj['Jan 1']
     
    # obj['Jan 2'] = 'Jan 2'
    # obj['Jan 3'] = 'Jan 3'
    # obj['Jan 4'] = 'Jan 4'
    # obj['Jan 5'] = 'Jan 5'
    
    # obj['MAY 30'] = 'MAY 30'
    # print(obj.arr)

