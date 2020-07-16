# << -------------- Food ordering system --------------------- >>
from queue import Queue
import time
import threading

__order_queue = Queue()
orders_list = ['pizza','samosa','pasta','biryani','burger']

def place_order(orders ):
    time.sleep(1)
    for order in orders:
        try: # These try and catch are optional, reserved for future implementation
            time.sleep(0.5)
            __order_queue.enqueue( order )
            print('{} order been placed'.format( order ) )
        except Exception as err:
            print(err)
            break
    
def serve_order():
    time.sleep(2)
    try:
        while True:
            if __order_queue.is_empty():
                print("No order left to be served!")
                break
            else:
                for item in range(__order_queue.size()):    
                    time.sleep(0.6)
                    print('{} have been served'.format( __order_queue.dequeue() ) )
    except Exception as err:
        print(err)
        
    
if __name__ == "__main__":
    place_order_thread = threading.Thread(target=place_order, args=(orders_list,) )
    serve_order_thread = threading.Thread(target=serve_order)

    place_order_thread.start()
    serve_order_thread.start()

    place_order_thread.join()
    place_order_thread.join()
    