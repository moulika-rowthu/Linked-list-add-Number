class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print("None")

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    
    def delete_begin(self):
        if self.head is None:
            print("List is already empty!")
            return
        self.head = self.head.next  

s1 = Single()
s1.add_end(10)
s1.add_end(20)
s1.add_end(30)
s1.add_end(40)

print("Original List:")
s1.display()


s1.delete_begin()

print("After deleting first node:")
s1.display()
