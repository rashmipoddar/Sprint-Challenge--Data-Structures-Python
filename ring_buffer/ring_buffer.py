from doubly_linked_list import DoublyLinkedList
from dll_queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        q = Queue()
        if self.capacity != self.storage.length:
            if self.storage.length == 0:
                self.storage.add_to_head(item)
                self.current = item
                q.enqueue(item)
            else:
                self.storage.add_to_tail(item)
                self.current = item
                q.enqueue(item)
        else:
            print(self.current)
            self.storage.remove_from_head()
            self.storage.add_to_head(item)  
        
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        print(self.storage.length)
        if self.storage.length is None:
            return list_buffer_contents
        current = self.storage.head
        print(current.value)
        while current:
            list_buffer_contents.append(current.value)
            if current.next: 
                current = current.next
            else: 
                break
        return list_buffer_contents
        
    


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


rb = RingBuffer(5)
# print(rb.get())
rb.append('a')
rb.append('b')
rb.append('c')
rb.append('d')
rb.append('e')
print('the array is ', rb.get())
rb.append('e')