from datetime import datetime  # Import for time handling

class NODE():
    def __init__(self,name,people,booking_time):
        self.name = name
        self.people = people
        self.booking_time = booking_time 
        self.next = None
    
class QUEUE():
    def __init__(self):
        self.head = None

    def Enqueue(self, name, people, booking_time):
        new = NODE(name, people, booking_time)
        if self.head is None:
            self.head = new
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new

    def Dequeue(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            node = self.head
            self.head = node.next

    def Print_test(self):
        queue = []
        if self.head is None:
            return ["Empty"]
        else:
            node = self.head
            while node:
                queue.append(f"{node.name} booking for {node.people} at {node.booking_time}")
                node = node.next
            return queue

    def is_empty(self):
        return self.head is None

    
    def is_empty(self):
        if self.head is None:
            return True
        return False
