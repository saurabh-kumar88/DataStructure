from queue import Queue

def print_binary(start, end):
        
    numbers = Queue()
    numbers.enqueue(str(1))
    for num in range(start, end):
        x = numbers.dequeue()
        print(x)
        numbers.enqueue(str(x) + '0')
        numbers.enqueue(str(x) + '1')
    

    
if __name__ == "__main__":
    print_binary(start=1, end=11)