from collections import deque
import time

# class Queue:

#     def __init__(self):
#         self.buffer = deque()
    
#     def __str__(self):
#         return "Simple container class for queue"
    
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
    
#     def dequeue(self):
#         return self.buffer.pop()
    
#     def front(self):
#         return(self.buffer.popleft())
    
#     def is_empty(self):
#         return (True if self.buffer.__len__() == 0 else False)
        
#     def size(self):
#         return len(self.buffer)


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self): 
        return ( "queue is empty" if self.is_empty() else self.buffer.pop()  )
            
    def is_empty(self):
        # a minor improvement
        return (True if self.buffer.__len__( )== 0 else False )

    def size(self):
        return len(self.buffer)


stock_price = Queue()

stock_price.enqueue({
    'company' : 'tcs',
    'timeStamp' : '15 apr , 11:04 am',
    'price' : 135.25,
})

stock_price.enqueue({
    'company' : 'google',
    'timeStamp' : '15 apr , 11:04 am',
    'price' : 125.4,
})

stock_price.enqueue({
    'company' : 'infy',
    'timeStamp' : '15 apr , 11:05 am',
    'price' : 98.17,
})

stock_price.enqueue({
    'company' : 'amazon',
    'timeStamp' : '15 apr , 11:06 am',
    'price' : 198.17,
})



if __name__ == "__main__":
    print( stock_price.size() )
    while True:
        time.sleep(1)
        if stock_price.is_empty():
            print("queue is empty")
            break
        else:
            print( stock_price.dequeue() )


 
    
    