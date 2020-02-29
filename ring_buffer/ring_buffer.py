from doubly_linked_list import DoublyLinkedList
from dll_queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity != self.storage.length:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail 
        else:
            if self.current.next:
                self.storage.delete(self.current.next)
                self.current.insert_after(item)
                self.storage.length += 1
                self.current = self.current.next
            else:
                self.current = self.storage.head
                self.storage.delete(self.current)
                self.storage.add_to_head(item)
                self.current = self.storage.head
        
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# rb = RingBuffer(5)
# rb.append('a')
# rb.append('b')
# rb.append('c')
# rb.append('d')
# rb.append('e')
# rb.append('f')
# print(rb.get())
# rb.append('g')
# print(rb.get())
# rb.append('h')
# print(rb.get())
# rb.append('i')
# rb.append('j')
# rb.append('k')
# print(rb.get())
# for i in range(50):
#     rb.append(i)
#     print(rb.get())