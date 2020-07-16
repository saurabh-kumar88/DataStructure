# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
      self.head = None 

    def insert_values(self, Array):
      self.head = None
      for item in Array:
        self.insert_at_end( item )
    
    def insert_at_end(self, data):
      if self.head is None:
        self.head = ListNode( data, None )
        return
      else:
        itr = self.head
        while(itr.next):
          itr = itr.next
        itr.next = ListNode(data, None)
      
    
    def printlist(self):
      if self.head is None:
        return "list is empty"
      
      itr = self.head
      llstr = ""
      
      while itr:
        llstr += str(itr.val) + "-->" 
        itr = itr.next
      
      print(llstr)

    "print even index value first then odd index val"

    


    def oddEvenList(self):
      
      "_____ TWO SPLIT EVEN AND ODD LINKED LIST APPROACH _____"
      
      # base case
      if self.head is None or self.head.next is None:
        return self.head

      odd_ll = ListNode(-1) # dummy odd linked list
      even_ll = ListNode(-1) # dummy even linked list

      odd = odd_ll # odd pointer
      even = even_ll # even pointer

      
      itr = self.head
      parity = True # True for odd index and False for even
      curr_odd = odd
      curr_even = even
      curr = self.head
      
      while curr:
        temp = curr
        curr = curr.next
        temp.next = None # breaking the connection
        
        if parity:
          curr_odd.next = temp
          curr_odd = curr_odd.next
        else:
          curr_even.next = temp
          curr_even = curr_even.next
        parity = not parity

      curr_odd.next = even_ll.next # merging two linked list
      self.head = odd_ll.next
      
      self.printlist()

        
values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
arr = [1,2,3,4,5,6,7,9,10]




if __name__ == "__main__":
  ll = Solution()
  ll.insert_values( values )
  # ll.printlist()
  ll.oddEvenList()


  




     
