class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '<-->'
            itr = itr.next
        
        print(llstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '<-->'
            itr = itr.prev
        print(dllstr)
    
    def insert_at_begginig(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node 

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr= self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begginig(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                node = Node(data, itr.next, itr) 
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            self.insert_at_begginig(data_to_insert)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next


    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        if itr.data == data:
            itr.next.prev = None
            self.head = itr.next
            return
        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_backward()
    ll.print_forward()
    ll.insert_after_value("mango","apple")
    ll.print_forward()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_forward()
    ll.insert_at(2, "pear")
    ll.print_forward()
    ll.remove_at(2)
    ll.print_forward()