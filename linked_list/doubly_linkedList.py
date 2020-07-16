
class Node:
    COUNTER = 0
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next  # next pointer
        self.prev = prev  # prev pointer
        Node.COUNTER += 1


class Linked_List:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
    # test code
    def get_size(self):
        return Node.COUNTER

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_begining(self, data):
        node = Node(data, self.head, self.tail)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        "Check if list is empty"
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if (index < 0) or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next 
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                "breaking the connection and setting it to next node"
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # create new node or insert data
                node = Node(data, itr.next)
                itr.next = node
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
                self.insert_at(count + 1, data_to_insert)
                matchFound = True
                break
            else:
                matchFound = False
            count += 1
            itr = itr.next
        if matchFound is False:
            raise Exception(value_after, " does not exist!")

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
            raise Exception(value_to_remove, " does not exist!")

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

    def print_backward(self):
        "Last node is necessary to traverse from backward"
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.get_last_node()
    
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev

        print("reverse order : {} ".format(llstr))

if __name__ == "__main__":
    ll = Linked_List()
    # ll.insert_at_begining(45)
    # ll.insert_at_begining(500)
    # ll.print()

    # ll.insert_at_end(217)
    # ll.insert_at_end(1025)
    # ll.print()

    ll.insert_values(['mango', 'apple', 'grapes', 'banana', 'figs'])
    ll.print()
    print("size of ll : {} ".format(Node.COUNTER) )
    #ll.print_backward()
    # ll.print()
    

    # print("length : ", ll.get_length())

    # ll.remove_at(1)
    # ll.print()

    # ll.insert_at(2, "11244")
    # ll.print()

    # ll.insert_after_value("grapes", "Jack fruit")
    # ll.print()

    # ll.remove_by_value("apple")
    # ll.print()
