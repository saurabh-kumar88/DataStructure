#_______________ Hash-map Implementation in python ______________________
#________________Collision handling : By using Chaining ______________________  

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range (self.MAX)]
    
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
        found = False
        # check if key is already present in linked list
        for idx, element in enumerate(self.arr[h]):            
            if len(element) == 2 and element[0] == key: # update key-value if already present
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val)) # or append new key-value pair to last
        
    
    def __getitem__(self, key):
        self.key = key
        h = self.get_key(key)
        found = False
        # Check if key exists
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                found = True
                return 'Value : {}'.format(element[1])
        if not found:
            raise Exception('{} is not a valid key'.format(self.key))
                
            
    def __delitem__(self, key):
        h = self.get_key(key)
        found = False
        # Check if key exists
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                found = True
                del self.arr[h][idx]
        if not found:
            raise Exception('{} is not a valid key'.format(key))
            
        
if __name__ == "__main__":
            
    obj = HashTable()

    # Adding 
    # obj['Jan 10'] = 100
    # obj['Feb 19'] = 150
    # obj['march 23'] = 200
    # obj['Apr 16'] = 175

    # Reading
    # print( obj['Jan 10'] )
    # print( obj['Feb 19'] )
    # print( obj['march 23'])

    # Updating
    # obj['Jan 10'] = 11
    # obj['Feb 19'] = 160

    # Deleting

    # del obj['Jan 10']
    # del obj['Feb 19']


    # ----- What is collision ? --> if two or more keys got same hash
    # <<-----------------For example : dates formats having same hash keys ---------------------->>
    # MAY 30 Jan 1
    # OCT 31 Jan 1
    # January 31 Jan 1
    # November 31 Jan 1

    # obj['Jan 1'] = 21
    # obj['APRIL 6'] = 135
    # obj['MAY 30'] = 46 
    # obj['January 31'] = 56 
    # obj['November 31'] = -710
    # obj.arr
