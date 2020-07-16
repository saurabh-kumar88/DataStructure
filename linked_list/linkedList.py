class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        # check if list is empty
        if self.head is None:
            self.head = Node(data, None)
            return
            
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        # returns length of linked list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_begining(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # create new node or insert data
                node = Node(data, itr.next)
                itr.next  = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, value_after, data_to_insert):
        # check if value exists
        itr = self.head
        count = 0
        matchFound = False
        while itr:
            if itr.data == value_after:
                self.insert_at( count + 1, data_to_insert )
                matchFound = True
                break
            else:
                matchFound = False
            count += 1
            itr = itr.next
        if matchFound is False:
            raise Exception(value_after , " does not exist!")
    
    def remove_by_value(self, value_to_remove):
        itr = self.head
        count = 0
        matchFound = False
        while itr:
            if itr.data == value_to_remove:
                self.remove_at(count)
                matchFound = True
                break
            else:
                matchFound = False
            count += 1
            itr = itr.next
        if matchFound is False:
            raise Exception(value_to_remove , " does not exist!")
                
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

if __name__ == "__main__":
    ll = Linked_List()
    # ll.insert_at_begining(11)
    # ll.insert_at_begining(22)
    # ll.insert_at_end(43)
    # ll.insert_at_end(54)
    # ll.print()

    # print original linked list
    ll.insert_values([1,2,3,4,5])
    ll.print()
    
    # #print("length : ", ll.get_length())
    
    # ll.remove_at(11)
    # ll.print()
    
    # ll.insert_at(1, "figs")
    # ll.print()
    
    # ll.insert_after_value("grape", "Jack fruit")
    # ll.print()

    # ll.remove_by_value("apple")
    # ll.print()

